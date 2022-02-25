
class MagicList(list):

    def __setitem__(self, inx, value):
        if inx < 0:
            raise IndexError('The Index most be positive.')

        if len(self) - 1 < inx:
            while len(self) < inx:
                # appending items until needed location is reached
                self.append(None)
            self.append(value)
        else:
            # when index within existed size of created list
            super(MagicList, self).__setitem__(inx, value)


if __name__ == '__main__':

    L = MagicList()
    L[1] = "Dan"
    L[6] = "Avi"
    L[3] = "Bonzo"

    # let's see what we have:
    print(L)

    # trying to create a negative index (should raise the IndexError error) :
    L[-1] = 'Putin'
