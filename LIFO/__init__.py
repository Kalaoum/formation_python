class MaPile:

    def __init__(self):
        self.pile = []

    def pile(self,args):
        print("ARGS",args,"\n",type(args))
        #for element in args:
        #    print("Element:",element)
        #    self.pile.append(element)
  #      return self.pile

    def empile(self,element):
        list_tempo = [ element ]
        list_tempo.extend(self.pile)
        self.pile = list_tempo

    def depile(self):
        self.pile.remove(self.pile[0])

    def test(self,element):
        self.pile.append(element)