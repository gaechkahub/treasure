
print('''
                    _,__        .:
            Darwin <*  /        | \\ 
               .-./     |.     :  :,
              /           '-._/     \\_
             /                '       \\
           .'                         *: Brisbane
        .-'                             ;
        |                               |
        \\                              /
         |                            /
   Perth  \\*        __.--._          /
           \\     _.'       \\:.       |
           >__,-'             \\_/*_.-'
                                 Melbourne
                                 ''')
print("Welcome to the game \"Treasure Island\".")
print("You are in Australia and your task is to \nfind a treasure here.")
choice1 = "\nYou are in the very center of the continent, in the \ndeserted desert. There are two roads in front of you - one \nleads to the South, the other to the North. \nWhat will you choose? \nSouth or North?\n"
choice2 = "\nYou have arrived at the outskirts of Melbourne, the \ncultural capital of Australia. You have no money, \nbut you really want to eat. What you will do is \nsteal some food from the nearest shop, \nwhose owner has been carelessly absent on business, or \nfind something edible in the junkyards near the \nsuburban houses.\nType what you chose - steal or beg?\n"
choice3 = "\nIn Australia, you can find anything \nanything in the junkyards - you find the rarest service of one of the \noldest Chinese Ming Dynasty, selling it on \nEbay, you become a millionaire. Now you need to \ndecide whether to continue searching for the treasure and head \nor to Brisbane , either to Perth, or stay \nMelbourne. \nType - stay, Perth or Brisbane?\n"
result1 = "\nYou decide that no one is looking for good and that you \nhave enough money for everything now and \nstay in Melbourne. You become imbued with \nAustralian culture and after a while you \ncompletely stop drinking, smoking, cheating and \ndeceiving. A few years later, you \nmeet your soulmate, with whom you live happily \nuntil your death. \nCongratulations, you've found your treasure! \nYou win!"
result2 = "\nWhen you arrive in Brisbane, of course, you immediately \ngo to the most famous surf spot in the world \nGold Coast, rent the best surfboard \nand go to conquer the waves. \nHowever, it might have been worth learning \n a little at the beginning - the very first wave \nknocks you down, spins you, you \nhit your head on a stone at the bottom and \ncause a traumatic brain injury incompatible with life. \nGame over."
result3 = "\nYou take the coolest sports car and drive to Perth in \na matter of days. However, soon \nyou begin to feel very unwell and \nremember how the compatriot with whom you \ncelebrated your departure coughed hoarsely all the way, \nsaying: \"Damned mines\". Obviously, \nthe mines were not to blame and you become \nthe second case of covid in Western \nAustralia. You are hospitalized, but even \nextra-specialists cannot cope with your \nrapidly progressing bilateral \npneumonia As you depart for the other world, you decide that \nnext incarnation you must not forget to drink less \nand probably not even start smoking. But \nfor now... \nGame over."
result4 = "\nThere was a camera in the shop, the owner called the \npolice and tried to detain you until they \narrived. Desperately trying to escape and hide, \nyou accidentally break the owner's nose, as a result you \nare tried not only for theft, but also for causing \n nmoderate damage to health.After lengthy \nlitigation, the first time you \nget off with a suspended sentence, but you \nare expelled from the country. \nGame over."
result5 = "\nBarringly plodding through the tropical jungle, \ntired and exhausted by the heat, you \nfinally reach the coast, joyfully \nplunge into the water, and... soon become the crocodile's \nbreakfast. \nGame over!"
error = "\nThis option does not exist.\nGame over!"
doroga = input(choice1).lower()
if doroga == "south":
   do = input(choice2).lower()
   if do == "beg":
     future = input(choice3).lower()
     if future == "stay":
       print(result1)
     elif future == "brisbane":
       print(result2)
     elif future == "perth":
       print(result3)
     else:
       print(error)
   elif do == "steal":
     print(result4)
   else:
     print(error)
elif doroga == "north":
   print(result5)
else:
   print(error)
