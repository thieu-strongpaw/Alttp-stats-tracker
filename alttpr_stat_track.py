## Matt Garcia
## This is a program to track stats from A Link to the Past
## Randomizer. It should manualy take input and display stats.

## Class for save file
class GameStatSave:
    ## initiate the class
    def __init__(self, mode, time, items, ganon, ped, dungeon_reward):
        self.__game_mode = mode
        self.__comp_time = time
        self.__item_comp = items
        self.__ganon_req = ganon
        self.__ped_req = ped
        self.__crystal_o_pendent = dungeon_reward
    
    ## All the "set" moduals
    def set_game_mode(self, mode):
        self.__game_mode = mode
    
    def set_comp_time(self, time):
        self.__comp_time = time
    
    def set_itme_comp(self, items):
        self.__item_comp = items

    ## This will be a boolean
    def set_ganon_req(self, ganon):
        self.__ganon_req = ganon

    ## This will be a boolean
    def set__ped_req(self, ped):
        self.__ped_req = ped

    ## I think that using a dictionary data type.
    ## the keys will be dungeon names and the data will be 
    ## pendent or crystal
    def set_crystal_o_pendent(self, dungeon_reward):
        self.__crystal_o_pendent = dungeon_reward

    ## All the "get" modules

    def get_game_mode(self):
        return self.__game_mode

    def get_comp_time(self):
        return self.__comp_time

    def get_item_comp(self):
        return self.__item_comp

    def get_ganon_req(self):
        return self.__ganon_req

    def get_ped_req(self):
        return self.__ped_req

    def get_crystal_o_pendent(self):
        return self.__crystal_o_pendent



    
dungeons = {'TT':'Pendent','MM':'Crystal'}

def main():
    print('lets start main()')

    save_1 = GameStatSave('basic', 2.55, 215, True, True, dungeons)
    print(save_1.get_ped_req())


main()
    