class Character:
    def __init__(self, name, location) -> None:
        self.name=name
        self.location=location
        self.observation=""
        self.items=[]
        self.skills={}
        self.stats={"strength":0, "intelligence":0, "agile":0, "luck":0}

class Place:
    def __init__(self, name, description="") -> None:
        self.name=name
        self.description = description

background={
    0:"A normal day, a boy woke up and is going to have his first school day.",
    1:"A boy is on his way to school."
}

place={
    0:[Place("living room"), Place("bedroom")],
    1:[Place("home"), Place("street"), Place("school")]

}

npc={
    0:[Character("John", "home")]
}

geo_map={
    0:{"living room":(0,0,0), "bedroom":(1,1,1)}
}
