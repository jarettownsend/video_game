def player_border_check(player):
    if player.xcor() < -490:
        player.setx(-490)
    if player.ycor() > 337.5:
        player.sety(337.5)
    if player.ycor() < -340:
        player.sety(-340)
    if player.xcor() < -410 and player.ycor() < 235:
        player.sety(235)
    if player.ycor() < 235 and player.xcor() < -390:
        player.setx(-390)
    if player.ycor() > -260 and player.xcor() > 390:
        player.setx(390)
    if player.xcor() > 390 and player.ycor() > -280:
        player.sety(-280)
