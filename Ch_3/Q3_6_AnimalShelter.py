class AnimalShelter():

    def __init__(self):

        self.in_time = 0
        self.dog_que = []
        self.cat_que = []

    def enqueue(self, animal, name):
        if animal == "cat":
            self.cat_que.append((name, self.in_time))
            self.in_time += 1
        elif animal == "dog":
            self.dog_que.append((name, self.in_time))
            self.in_time += 1

    def dequeueAny(self):
        # 어느 한쪽만 빈경우 두 가지
        if not self.dog_que and self.cat_que:
            go = self.cat_que[0]
            self.cat_que = self.cat_que[1:]
            return go
        elif not self.cat_que and self.dog_que:
            go = self.dog_que[0]
            self.dog_que = self.dog_que[1:]
            return go
        # 둘 다 빈 경우
        elif not self.dog_que and not self.cat_que:
           raise Exception("No animal in Shelter")
        # 둘 다 동물이 차 있는 경우
        else:
            dog_first = self.dog_que[0]
            cat_first = self.cat_que[0]
            # in_time이 작은 동물이 빨리 들어온 동물 == 먼저 나가야 할 동물
            if dog_first[1] < cat_first[1]:
                self.dog_que = self.dog_que[1:]
                return dog_first[0]
            else:
                self.cat_que = self.cat_que[1:]
                return cat_first[0]

    def dequeueDog(self):
        if self.dog_que:
           dog = self.dog_que[0]
           self.dog_que = self.dog_que[1:]
           return dog[0]
        else:
            raise Exception("No Dog in Shelter")

    def dequeueCat(self):
        if self.cat_que:
            cat = self.cat_que[0]
            self.cat_que = self.cat_que[1:]
            return cat[0]
        else:
            raise Exception("No Cat in Shelter")


def test_animal():
    shelter = AnimalShelter()
    shelter.enqueue('cat','cat0')
    shelter.enqueue('cat','cat1')
    shelter.enqueue('dog','dog0')
    shelter.enqueue('dog','dog1')
    shelter.enqueue('cat','cat2')
    shelter.enqueue('dog','dog2')
    print(shelter.dog_que)
    print(shelter.cat_que)
    print(shelter.dequeueAny())
    print(shelter.dequeueCat())
    print(shelter.dequeueDog())


test_animal()
