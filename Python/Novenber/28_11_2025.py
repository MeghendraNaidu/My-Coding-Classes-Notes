# # Matplotlib
# # 1. For graphs and visualisations of data analysis, reports and scientific plots.


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]
# #Gives you a line plot
# plt.plot(x, y)
# plt.show()



# title()
# xlabel('X-axis')
# ylabel('Y-axis')





# plt.plot(x, y, color='red', linestyle='--', marker = 'o')
# #color => red, purple, yellow, #FF5733
# #marker = 
# 	'o' (Circle)
# 	's' (Square)
# 	'^' (Traingle Up)
# 	'v' ('Traingle Down')
# 	'*' (Star)
# 	'+' (Plus)
# 	'x' (Cross)
# 	'd' (Diamond)
# 	'p' (Pentagon)


# #linestyles => '-' solid
# #	    => '--' dashed
# #           => '-.' dashdot
# #           => ':' dotted


# #shortcut
# plt.plot(x, y1, 'ro--') #red color, circle marker and dashed line


# #Multiple plots on same graph
# plot(x, y1)
# plot(x, y2)
# show()


# plt.plot(x, np.sin(x), label="Sine")
# plt.plot(x, np.cos(x), label="Cosine")
# plt.legend(loc="upper right")




# .bar(x, y, color='green')
# .scatter(x, y)
# pie => See how it works

# sizes = [25, 30, 20, 25]
# sectors = ['A', 'B', 'C', 'D']

# plt.pie(x = sizes, labels = sectors, startangle=90)
# plt.show()
# autopct='%1.1f%%

# #plt.figure(figsize=(8, 5)) 




# plt.savfig('my_plot.png')





# fig, axs = plt.subplots(1, 2)
# fig is the container 
# axs - array of 2 axes objects
# axs[0].plot(x,y1)
# axs[0].set_title('Linear')
# axs[1].bar(x, y2)
# axs[1].set_tile('Quadratic')

# #How to apply grid, x axis, y axis, title to each one of these se
# plt.show()



# fig, axs = plt.subplots(2, 2, figsize(8, 6))
# axs[0, 0].plot(x, y)
# axs[0][0].set_title('Line')





# #Adjusts
# plt.tight_layout()
# plt.grid(visible=True, linestyle="--", alpha=0.6)

# plt.style.use('seaborn-v0_8-darkgrid')
# ['classic', 'ggplot', 'Solarize_Light2', 'seaborn-v0_8-paper', 'dark_background', 'fast', 'bmh', 'grayscale']

# plt.text(3, 10, "This point is important", fontsize=10, color="red")
# plt.annotate("Peak", xy=(5,25), xytext=(3,20),  arrowprops=dict(facecolor='black', arrowstyle="->"))