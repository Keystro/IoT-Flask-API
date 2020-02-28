This flask-api was part of a school project for testing our skills with embedded systems and system programming
The project itself as a Smart Street Lighting System with IoT.
The system itself is autonomus works on a basic program mostly composed of if statements.
Give a set of variables as voltage it compares it in 2 categories both High and Low 
sample code below

        '''
        High = 4
        Low = 1
        data = 0
        for I in range of (data):
            if I =< Low:
                Lights_On()
            elif I => High:
                Lights_Off()
            else:
                return NULL
        '''

The IoT device uses a server to write data to this API and the data is stored in a dtababse and dispalyed in a page
the advantages is thourgh this connection one can monitor all the components of the IoT device without having to physically check the device.
