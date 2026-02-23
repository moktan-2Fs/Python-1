class Tamang:
    falls_in = "Tamang"

    def __init__(self, group, no_of_members):
        self.group = group
        self.no_of_mems = no_of_members

    def __len__(self):
        return len(self.group)

    def area(self, are):
        return f"Hello there,I am {self.falls_in}, and fall in {self.group} group of {self.falls_in} and am from {are}...\nAlso not to mention there are {self.no_of_mems} members in this group..\n Its nice to meet you.."


class Moktan(Tamang):
    father_group = "Moktan"

    def __init__(self, mother_group, no_of_siblings,):
        super(Moktan, self).__init__('Moktttttan', 30)
        self.mot_gro = mother_group
        self.no_of_sib = no_of_siblings

    def printing(self):
        print(self.area("Manang"))
        print(super(Moktan, self).__len__())
        return f"{self.mot_gro}, {self.no_of_sib}, {self.group}, {self.no_of_mems}"


mok = Tamang("Moktan", 40)
print(mok.area("Dolakha"))

sagar = Moktan("Rumba", 3)
# sagar.printing()
print(sagar.printing())
