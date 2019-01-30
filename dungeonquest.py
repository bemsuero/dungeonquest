from sys import exit
from random import randint
from textwrap import dedent

    # if character == 'wizard':
    # elif character == 'fighter':
    # elif character == 'rogue':
    # else:

def main():
    character = "Human"
    print("Choose your class! Wizard, Fighter, or Rogue.")
    character = input(">").lower()

    if character != "wizard" and character != "fighter" and character != "rogue":
        print("This dungeon is too dangerous without a class.")
        main()

    print(f"You have chosen a {character}")

    class Scene(object):

        def enter(self):
            print("This scene is not yet configured.")
            print("Subclass it and implement enter().")
            exit(1)

    class Engine(object):

        def __init__(self, scene_map):
            self.scene_map = scene_map

        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('finished')

            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

    class Death(Scene):

        quips = [
            "You died.",
            "You didn't live.",
            "Dead for the first time, again.",
            "You take the big sleep.",
            "You fell through life into death."


        ]

        def enter(self):
            print(Death.quips[randint(0, len(self.quips)-1)])
            exit(1)

    class EnterDungeon(Scene):

        def enter(self):
            print(dedent("""
                You see a dungeon before you and know that your destiny nears.
                Do you dare go inside? 'Enter' or 'Leave', the choice is yours.
                Going forward enter your choices carefully, as a wrong move may cost
                you your life. 
                """))

            if character == 'wizard':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You saunter in, your robes flowing in the wind. Your spellbook
                        is clutched in your hand, as you anticipate the adventure that
                        is ready to begin.
                        """))
                    return "first_encounter"

                elif action == "leave":
                    print(dedent("""
                        You turn back, unprepared for the horrors that are right behind you.
                        """))
                    return "death"

                else:
                    print("Your indecision has cost you your life.")
                    return "death"

            elif character == 'fighter':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You keep your short sword ready at your side as you start walking toward
                        the entrance. You are wary of the monsters and ghouls who are said
                        to live in these walls. You are brave above all.
                        """))
                    return "first_encounter"

                elif action == "leave":
                    print(dedent("""
                        You turn back, unprepared for the horrors that are right behind you.
                        """))
                    return "death"

                else:
                    print("Your indecision has cost you your life.")
                    return "death"

            elif character == 'rogue':
                action = input("> ").lower()

                if action == "enter":
                    print(dedent("""
                        You walk along the shadows, dagger hidden. You are aware of the traps
                        that might be around every corner. Tricks and treats were always your
                        forte.
                        """))
                    return "first_encounter"

                elif action == "leave":
                    print(dedent("""
                        You turn back, unprepared for the horrors that are right behind you.
                        """))
                    return "death"

                else:
                    print("Your indecision has cost you your life.")
                    return "death"

    class FirstEncounter(Scene):

        def enter(self):
            print(dedent("""
                You enter the hallowed halls of the dungeon. The air is thick with the stench
                of old wood and rottng flesh. You glance around. Nothing seems to have been
                touched for a long time. If other adventurers came through here, there is no
                longer a trace of them. As you walk into the northern hall, you come across an
                opening with a thirty foot ceiling. In the middle of the room you see a shambling
                body. As soon as you see it, it turns around. A zombie approaches!
                """))

            if character == "wizard":
                print(dedent("""
                    You shudder in fear. The school prepared you for this, but you have never seen
                    a zombie up close. You consider what you can do. Should you 'yell' for it to stop?
                    Should you cast 'magic missile'? Should you 'run' away?
                    """))
                action = input("> ").lower()

                if action == "yell":
                    print(dedent("""
                        'STOP FIEND', you yell out. The zombie doesn't seem to have any manners.
                        It lurches forward and grabs on to you. Maybe yelling at a zombie wasn't
                        such a good idea.
                        """))
                    return "death"

                elif action == "magic missile":
                    print(dedent("""
                        Your 3 missiles all hit the creature. The first stuns him, the second stops
                        him completely, and the last cracks the creatures skull open. The body falls
                        limp and it seems to have died for the final time. You breathe a sigh of relief.
                        """))
                    return 'mimic_room'

                elif action == "run":
                    print(dedent("""
                        'No treasure is worth my life', you think. You turn around to high-tail it
                        out of the dungeon. You take the first left, then another left. You feel
                        like you may have went the wrong way. As you stand contemplating why you
                        didn't draw a map, you feel a cold hand on your shoulder.
                        """))
                    return "death"

                else:
                    print("Your indecision has cost you your life.")
                    return "death"

            elif character == "fighter":
                print(dedent("""
                    You expected horrors so you are not surprised. Your warrior spirit urges you
                    forward. The only option is attack. You bring the short sword up to take down
                    the abomination. Should you cut off it's 'arms' to stop it's attack? Go for the
                    'legs' and hinder it's mobility? Or should you go straight for the 'head', and
                    end it's misery?
                    """))
                action = input("> ").lower()

                if action == "arms":
                    print(dedent("""
                        You swing wildly at the creature's arm. It comes clean off. As you swing
                        down onto the other arm you lose momentum. The blade gets caught halfway
                        through the shoulder. As you struggle to get it off the zombie rears forward
                        and sinks his teeth into your neck.
                        """))
                    return "death"

                elif action == "legs":
                    print(dedent("""
                        'It can not eat me if it can not catch me', you chuckle to yourself.
                        You lunge forward, and do a horizontal attack towards the creature's
                        left leg. The blade sinks into it's hip and gets stuck. As you try to yank
                        it out, the creature grabs a hold of you. The last thing you see is a dirty
                        grin.
                        """))
                    return "death"

                elif action == "head":
                    print(dedent("""
                        A classic villain deserves a classic approach. You run forward and leap
                        into the air. Screaming, you plunge your sword into the zombie's skull. It
                        gasps like it needs air and collapses. Foolish creature thought that it could
                        get through you.
                        """))
                    return "mimic_room"

            elif character == "rogue":
                print(dedent("""
                    'Well, this is a sticky situation.', you think to yourself. 'I am not exactly the
                    fighting type.' Your options are not limited, however. You consider 'running' and getting
                    a better position. You think that maybe you could 'slice' up this particular foe, as
                    he seems slow. A last resort is to somehow 'sneak' by it. How good could the senses of
                    an undead be?
                    """))
                action = input("> ").lower()

                if action == "running":
                    print(dedent("""
                        You turn back and run around the corner. You hear the shambling of the creature as
                        it gets closer and closer. It seems like it can either hear your breathing, or smell
                        the metal hidden in your cloak. The waiting seems eternal. You take one deep breath
                        and as it turns the corner you plunge your dagger into it's face. That seems to be enough
                        to take it down. Good thing you're not a fighter.
                        """))
                    return "mimic_room"

                if action == "slice":
                    print(dedent("""
                        Confident that you are quicker than this fiend, you run up and start hacking at it
                        with your hidden dagger. You slice up and down his body, not missing one vital point.
                        You are sure that after this barrage of blows not a single living creature would be
                        standing. Unfortunately for you this creature is not living. It grabs you with it's bloody
                        limbs.
                        """))
                    return "death"

                if action == "sneak":
                    print(dedent("""
                        'It turning around was probably a coincidence', you think. You slowly duck down and
                        start making your way towards the creature. It doesn't break it's gaze on you, but
                        you figure that it is not smart enough to do anything. As you slowly sneak past it you
                        breath a sigh of relief that it hasn't moved. You pat yourself on the back for a job well
                        done. Then you feel another, colder, hand on your back.
                        """))
                    return "death"

    class MimicRoom(Scene):

        def enter(self):
            print(dedent("""
                You make your way past the pile of zombie. Past where the creature was standing
                is a door adorned with golden trim. You carefully check the door. No traps, and
                it's not locked. Those are good signs. Looks like a fairly normal door aside from
                the gold. You open it carefully and two chests sit at the far end of an otherwise
                unremarkable room. There is what seems to be an exit behind the chests.
                """))

            if character == "wizard":
                print(dedent("""
                    'Knowledge will only get me so far', you think, 'Gold will buy plenty of
                    books.' You near both chests and take a look at them. The one on the 'left'
                    seems to be have built many years ago. You have seen chests in your history
                    books and it seems pretty standard. The one on the 'right', however, is
                    shiny and almost new. Surely the higher quality items would be in a higher
                    quality chest?
                    """))
                action = input("> ").lower()

                if action == "left":
                    print(dedent("""
                        You go over to the chest on the left. You cast acid splash on the lock
                        and it melts off. You open it to see a couple of bags of gold. You put
                        them into your backpack and head towards the exit and the other chest.
                        As you walk closer you seem to hear what sounds like the other
                        chest... sneezing? Best to move on.
                        """))
                    return "finished"

                if action == "right":
                    print(dedent("""
                        You go over to the chest on the right. You cast acid splash on the lock
                        and suddenly the chest bursts open. It reveals giant teeth and with a
                        shriek bites down. The last thing you feel is the acid around your body.
                        """))
                    return "death"

                else:
                    print("As you stand and try to make a decision the right chest lunges forward...")
                    return "death"

            elif character == "fighter":
                print(dedent("""
                    'This is what I am here for!', you laugh into the empty room. The two chests seem
                    to look the same. You figure that you will get both sets of loot and make
                    your way to the exit in the back. The chest on the 'right' is bigger than any you
                    have seen before. Maybe bigger than any chest should be but that means that there
                    has to be more treasure in it. The chest on the 'left' is standard size. It could
                    wait.
                    """))
                action = input("> ").lower()

                if action == "left":
                    print(dedent("""
                        Your armor clanks as you walk over to the chest on the left. You bring your short
                        sword down onto the lock, and it breaks rather easily. Inside you find two bags
                        of gold which you put into your backpack. As you walk over to the larger chest you
                        hear it sneeze. Maybe it's best if you move towards the exit.
                        """))
                    return "finished"

                elif action == "right":
                    print(dedent("""
                        You lunge into the air to bring your sword down onto the lock attached to the giant
                        chest. Almost if cued it opens revealing a set of teeth. You land inside the chest and
                        the last thing you feel is acid all around you as it closes it's mouth.
                        """))
                    return "death"

                else:
                    print("As you stand and try to make a decision the right chest lunges forward...")
                    return "death"

            elif character == "rogue":
                print(dedent("""
                    You glance at both chests. The 'left' chest seems to be a standard chest. It's lock seems
                    pretty easy to to pick. The 'right' chest is bigger, but a peculiar thing is that the lock
                    has no key hole. Maybe it's an enchanted lock?
                    """))
                action = input("> ").lower()

                if action == "left":
                    print(dedent("""
                        You pick the lock rather easily. Inside you find two bags of gold. You place them into
                        your backpack and move towards the exit. A lock with no keyhole is a little suspicious.
                        As you near the exit you hear the other chest sneeze. You made a good choice.
                        """))
                    return "finished"

                elif action == "right":
                    print(dedent("""
                        You are pretty confident you can pick any lock. As soon as grab the lock your hand gets
                        stuck. The chest opens up and bites down onto your body. You only see a flash of teeth
                        as you black out.
                        """))
                    return "death"

                else:
                    print("As you stand and try to make a decision the right chest lunges forward...")
                    return "death"

    class Finished(Scene):

        def enter(self):
            print("You won! Good job.")
            return "finished"

    class Map(object):

        scenes = {
            'enter_dungeon': EnterDungeon(),
            'first_encounter': FirstEncounter(),
            'mimic_room': MimicRoom(),
            'death': Death(),
            'finished': Finished(),
        }

        def __init__(self, start_scene):
            self.start_scene = start_scene

        def next_scene(self, scene_name):
            val = Map.scenes.get(scene_name)
            return val

        def opening_scene(self):
            return self.next_scene(self.start_scene)

    a_map = Map('enter_dungeon')
    a_game = Engine(a_map)
    a_game.play()

main()
