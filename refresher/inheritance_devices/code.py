class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connection_status = True

    def __str__(self):
        return f"Device {self.name!r}connected by --> ({self.connected_by})"

    def disconnected(self):
        self.connection_status = False
        print('Disconnected.')


class Printer(Device):
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining...)'
    
    def print(self, pages):
        if not self.connection_status:
            print("Your printer is not connected!!")
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages

######## Execute Program ###########
# device = Device('Printer', 'USB')
# print(device)
# device.disconnected()
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()
printer.print(20)


