#First Github Project.
#You should create a virtual env and pip install Matplotlib. Tkinter comes default with python.
#Then code away..

from tkinter import *

def plot_graph():
    #this is to get inputs from the entry widgets.
    def get_inputs():
        x_readings = x_entry.get()
        y_readings = y_entry.get()
       #print("X is:",x_readings,"\nWhile Y is:",y_readings)
        return x_readings, y_readings

    #this is to split it into an array.
    def convert_to_array(x_readings, y_readings):
        x_array = x_readings.split(",")
        #print("The x array is = ",x_array)

        y_array = y_readings.split(",")
        #print("The y array is = ", y_array)
        return (x_array, y_array)

    #This is to convert array to integer.
    def convert_array_content_to_int(x_array_, y_array_):
        x_array_int = []
        for content in x_array_:
            int_version = int(content)
            x_array_int.append(int_version)

        y_array_int = []
        for content in y_array_:
            int_version = int(content)
            y_array_int.append(int_version)

        #print(x_array_int)
        #print(y_array_int)
        return (x_array_int,y_array_int)

     #I thought this would be necessary, but it wasn't..but I left it here eitherway.
    def get_max_values(x_array,y_array):
        x_max_value = 0
        for value in x_array:
            if x_max_value > value:
                pass
            else:
                x_max_value = value

        y_max_value = 0
        for value in y_array:
            if y_max_value > value:
                pass
            else:
                y_max_value = value

        #print("X maximum value is: ",x_max_value,"\nY maximum value is:",y_max_value)
        return (x_max_value,y_max_value)

    #This is to plot the graph usnig matplotlib and the inputs.
    def plot_graph_(x_array,y_array):
        import matplotlib.pyplot as plt

        plt.plot(x_array, y_array)
        plt.show()

    returned_inputs = get_inputs()
    #print(returned_inputs)
    returned_inputs_as_Array = convert_to_array(returned_inputs[0],returned_inputs[1])
    #print(returned_inputs_as_Array)
    returned_int_arrays = convert_array_content_to_int(returned_inputs_as_Array[0],returned_inputs_as_Array[1])
    #x_and_y_maximum_value = get_max_values(returned_int_arrays[0],returned_int_arrays[1])
    plot_graph_(returned_int_arrays[0],returned_int_arrays[1])


print("This Terminal or Command Prompt is for Displaying errors.\n Post the errors on Lawrenceorolobo github.\n")

#The GUI codes start here.
root = Tk()
root.minsize(500,500)
root.maxsize(500,500)

#Below is for the display label.
attention_label = Label(root,text = "Please input the readings below.\nSeperate each reading by a comma (',').\n")
attention_label.pack(side = "top")

#The below is the frame for the input fields.
input_frame = Frame(root)
input_frame.pack(side = "top")

#below are the input fields and respected labels.
x_label = Label(input_frame, text = "X-axis = ")
x_label.grid(row = 0, column = 0)

x_entry = Entry(input_frame)
x_entry.grid(row = 0, column = 1)

y_label = Label(input_frame, text = "Y-axis = ")
y_label.grid(row = 1, column = 0)

y_entry = Entry(input_frame)
y_entry.grid(row = 1, column = 1)

#This is the button to plot the graph.
plotbutton = Button(root, text = "PLOT GRAPH.", padx = "50px", command = plot_graph)
plotbutton.pack(side = "top", pady = "50px")
#plotbutton.bind("<Button-1>", get_inputs)

root.mainloop()