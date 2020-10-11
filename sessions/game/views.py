from django.http import HttpResponse
from django.shortcuts import render, redirect
from game.models import Game, Player, PlayerGameInfo
from game.forms import PlayerGameInfoForm, PlayerTryForm


def show_home(request):

    show = False

    if Game.objects.filter(exists=True) and Game.objects.filter(exists=True).first().iniciator != request.session.get('user'):

        side = False

        info = Game.objects.filter(exists=True)

        info = info.first()

        show = True

        if 'user' not in request.session.keys():
            player = Player.objects.create()
            m2 = PlayerGameInfo.objects.create(player=player, game=info)
            request.session['user'] = player.id

        if request.method == 'POST':
            info_to_try = PlayerTryForm(request.POST)
            if info_to_try.is_valid():
                info.guess_count = info_to_try.cleaned_data['guess_count']
                info.save()
                return redirect('show')

        form = PlayerTryForm()

        hidden_number = info.hidden_number

        guess_count = info.guess_count

        if hidden_number and guess_count:

            if hidden_number < guess_count:
                guess = f'Загаданное число < {guess_count}'

            elif hidden_number > guess_count:
                guess = f'Загаданное число > {guess_count}'

            else:
                guess = f'Вы угадали число'
                info.exists = False
                info.save()

            try_count = info.player_try_count
            info.player_try_count = try_count + 1
            info.save()

        else:
            guess = 'вы еще не угадывали'

        return render(request, 'home.html', context={'form': form, 'stat': guess, 'side': side, 'show': show})

    else:
        form = PlayerGameInfoForm()
        statistic = None
        side = True

        if 'user' not in request.session.keys():
            player = Player.objects.create()
            request.session['user'] = player.id
        if 'game' not in request.session.keys():
            game = Game.objects.create()
            request.session['game'] = game.id
            game.iniciator = request.session['user']
            game.save()

            show = True

            form = PlayerGameInfoForm()

            statistic = "a"

        user_id = Player.objects.get(id=request.session['user'])

        game_id = Game.objects.get(id=request.session['game'])

        if request.method == 'POST':
            info = PlayerGameInfoForm(request.POST)
            if info.is_valid():
                game_id.hidden_number = info.cleaned_data['count']
                game_id.save()
                relationship = PlayerGameInfo.objects.create(player=user_id, game=game_id)
                return redirect('show')

        if game_id.exists == False:
            statistic = game_id.player_try_count

    return render(request, 'home.html', context={'form': form, 'stat': statistic, 'show': show, 'side': side})
