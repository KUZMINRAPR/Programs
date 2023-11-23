class String(str) :
    def __len__(self) -> int:
        return super().__len__()
    def __eq__(self, __value: object) -> bool:
        if((self[self.__len__() - 1] == 's' or self[self.__len__()-2:self.__len__()-1] == 'es' or self[self.__len__()-4:self.__len__()-1] == 'ing') or 
           __value[__value.__len__() - 1] == 's' or __value[__value.__len__()-2:__value.__len__()-1] == 'es' or __value[__value.__len__()-4:__value.__len__()-1] == 'ing'):
            return True;
        else:
            return super().__eq__(__value)
string_1 = String("apple")
string_2 = String("appleing")
print(string_1 == string_2)
