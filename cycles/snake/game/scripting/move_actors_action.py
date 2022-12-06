from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    def excecute(self, cast, script):
        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()

