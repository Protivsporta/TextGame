import Entity 

class World:

    def __init__ (self):
        
        Hero = Entity.MainHero(100,20)
        Mech = Entity.Weapon('меч',20)
        Krovosos = Entity.Characters(40,65)
        HichniyUeber = Entity.Characters(40,65)
        Key = Entity.Entity('ключ')
        Fakel = Entity.Entity('факел')
        Inventory = []    

        for i in range(1,6):
            
            if i == 1:
                print('В погоне за сокровищами капитана Пистолетова ты оказался в подземелье. Ты ранен в левую руку, так что можешь пользоваться только правой. Осматривая помещение, находишь сундук с двумя предметами: ', Mech.name, ',', Fakel.name, '. Ты можешь взять только один из них! Факел даст тебе возможность легче осматривать комнаты, меч в свою очередь даст тебе 20 единиц дополнительного урона. Введи имя предмета, который хочешь взять!')
                for n in range(0,5):
                    choice1 = input().lower()
                    if choice1 == Fakel.name:
                        Inventory.append(Fakel.name)
                        break
                    elif choice1 == Mech.name:
                        Hero.dmg += Mech.dmg
                        Inventory.append(Mech.name)
                        break
                    elif n == 4:
                        raise SystemExit('Game Over')
                    else:
                        print('меч или факел?')
                print('Хороший выбор!')
                print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                print("Чтобы пройти в следующую комнату введи 'идти'")
                for j in range(0,5):
                    gonext = input().lower()
                    if gonext == 'идти':
                        break
                    elif j == 4:
                        raise SystemExit('Game Over')
                    else:
                        print("'Идти', бля")
                        continue


            if i == 2:
                print('Ты оказался в следующей комнате. Присмотревшись, ты видишь в углу комнаты задремавшего Кровососа. Ты потревожил его сон и Кровосос недоволен. Ты можешь драться с ним или попытаться проскочить в следующую комнату.', '\n', 'Выбери "драться" или "проскочить"')
                choice2 = input().lower()
                
                if choice2 == 'драться' and Mech.name in Inventory:
                    print('Ты легко убиваешь Кровососа с помощью меча. Можешь идти дальше!')
                    print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                    print("Чтобы пройти в следующую комнату введи 'идти'")
                    for j in range(0,5):
                        gonext = input().lower()
                        if gonext == 'идти':
                            break
                        elif j == 4:
                            raise SystemExit('Game Over')
                        else:
                            print("'Идти', бля")
                            continue
                
                if choice2 == 'драться' and Mech.name not in Inventory:
                    print('Ты погибаешь в неравной схватке')
                    raise SystemExit('Game Over')

                if choice2 == 'проскочить' and Fakel.name in Inventory:
                    print('Ты бежишь изо всех сил и успеваешь в последний момент закрыть дверь прямо перед носом Кровососа.')
                    print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                    print("Чтобы пройти в следующую комнату введи 'идти'")
                    for j in range(0,5):
                        gonext = input().lower()
                        if gonext == 'идти':
                            break
                        elif j == 4:
                            raise SystemExit('Game Over')
                        else:
                            print("'Идти', бля")
                            continue

                if choice2 == 'проскочить' and Fakel.name not in Inventory:
                    print('Ты бежишь изо всех сил, но тяжелый меч замедляет тебя. Ты успеваешь проскочить, но Кровосос ранит тебя и снимает 25 единиц здоровья')
                    Hero.hp -= Krovosos.dmg
                    print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                    print("Чтобы пройти в следующую комнату введи 'идти'")
                    for j in range(0,5):
                        gonext = input().lower()
                        if gonext == 'идти':
                            break
                        elif j == 4:
                            raise SystemExit('Game Over')
                        else:
                            print("'Идти', бля")
                            continue

                else:
                    raise SystemExit('Game Over')

            if i == 3:
                print('Ты оказываешься в третьей комнате, посередине комнаты стоят два стула. На одном из них сидит Морфеус с вытянутыми вперед руками. Подходя ближе ты понимаешь, что сейчас придется сделать выбор. "синяя" или "красная"?')
                choice3 = input().lower()
                
                if choice3 == 'синяя':
                    print('Морфеус встает и эпично раздает тебе с вертухи по ебальнику. Морфеус не любит синий цвет')
                    raise SystemExit('Game Over')

                if choice3 == 'красная':
                    print('Морфеус одобрительно покачивает головой и дает тебе пройти дальше.')
                    print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                    print("Чтобы пройти в следующую комнату введи 'идти'")
                    for j in range(0,5):
                        gonext = input().lower()
                        if gonext == 'идти':
                            break
                        elif j == 4:
                            raise SystemExit('Game Over')
                        else:
                            print("'Идти', бля")
                            continue

                else:
                    raise SystemExit('Game Over')                    

            if i == 4:
                print('Входя в комнату ты мгновенно чувствуешь запах гнилого мяса. Интуиция подсказывает тебе: где-то поблизости прячется один из самых кровожадных убийц здешних мест. Сделав еще несколько шагов ты замечаешь атласную тень на стене напротив. Знакомые силуэты проносятся в голове и ты понимаешь, что это ОН. Хищный Уёбер. Дураку понятно, что драться бессмысленно. Но ты вспоминаешь, что Уёбер питает слабость к бородатым анекдотам. Вспоминаешь два: про Марью Ивановну(1) и про Лупу и Пупу(2). Какой расскажешь?')
                print('Нужно ввести цифру')
                for m in range(0,5):
                    choice4 = int(input())
                
                    if choice4 == 1:
                        print('Юмореска хорошая, но Уёбер не любил ходить в школу. В его голове появляются флешбэки, он злится и убивает тебя.')
                        raise SystemExit('Game Over')

                    if choice4 == 2:
                        print('Уёбер орет во весь голос. Когда он успокаивается, решает дать тебе ключ от заветной двери на волю!')        
                        Inventory.append(Key.name)
                        print(' Твое здоровье: ', Hero.hp, '\n', 'Твой урон: ', Hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(Inventory))
                        print("Чтобы пройти в следующую комнату введи 'идти'")
                        for j in range(0,5):
                            gonext = input().lower()
                            if gonext == 'идти':
                                break
                            elif j == 4:
                                raise SystemExit('Game Over')
                            else:
                                print("'Идти', бля")
                                continue
                        break
                    
                    elif m == 4:
                        raise SystemExit('Game Over')  

            if i == 5:
                print('Вот ты и у заветной двери. Это было славное приключение, прощай!')
                raise SystemExit('Game Over')








    				





