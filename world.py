import entity 

class World:

    def __init__ (self):
        
        hero = entity.MainHero(100,20)
        mech = entity.Weapon('меч',20)
        krovosos = entity.Character(40,65)
        hichniyueber = entity.Character(40,65)
        key = entity.Entity('ключ')
        fakel = entity.Entity('факел')
        inventory = []    

        for i in range(1,6):
            
            if i == 1:
                print('В погоне за сокровищами капитана Пистолетова ты оказался в подземелье. Ты ранен в левую руку, так что можешь пользоваться только правой. Осматривая помещение, находишь сундук с двумя предметами: ', mech.name, ',', fakel.name, '. Ты можешь взять только один из них! Факел даст тебе возможность легче осматривать комнаты, меч в свою очередь даст тебе 20 единиц дополнительного урона. Введи имя предмета, который хочешь взять!')
                for n in range(0,5):
                    choice1 = input().lower()
                    if choice1 == fakel.name:
                        inventory.append(fakel.name)
                        break
                    elif choice1 == mech.name:
                        hero.dmg += mech.dmg
                        inventory.append(mech.name)
                        break
                    elif n == 4:
                        raise SystemExit('Game Over')
                    else:
                        print('меч или факел?')
                print('Хороший выбор!')
                print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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
                
                if choice2 == 'драться' and mech.name in inventory:
                    print('Ты легко убиваешь Кровососа с помощью меча. Можешь идти дальше!')
                    print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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
                
                if choice2 == 'драться' and mech.name not in inventory:
                    print('Ты погибаешь в неравной схватке')
                    raise SystemExit('Game Over')

                if choice2 == 'проскочить' and fakel.name in inventory:
                    print('Ты бежишь изо всех сил и успеваешь в последний момент закрыть дверь прямо перед носом Кровососа.')
                    print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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

                if choice2 == 'проскочить' and fakel.name not in inventory:
                    print('Ты бежишь изо всех сил, но тяжелый меч замедляет тебя. Ты успеваешь проскочить, но Кровосос ранит тебя и снимает 25 единиц здоровья')
                    hero.hp -= krovosos.dmg
                    print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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
                    print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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
                        inventory.append(key.name)
                        print(' Твое здоровье: ', hero.hp, '\n', 'Твой урон: ', hero.dmg, '\n', 'Твой инвентарь: ', ', '.join(inventory))
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








    				





