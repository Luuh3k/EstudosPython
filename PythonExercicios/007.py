larg = float (input('largua da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print ('sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg,alt, área))
tinta = área / 2
print('Para pintar essa parede, você vai precisar de {}l de tinta.'.format(tinta))