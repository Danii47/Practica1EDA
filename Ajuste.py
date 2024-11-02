import numpy as np
import matplotlib.pyplot as plt

x = np.array([ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000 ])  # Reemplaza ... con tus 100 valores de x
y = np.array([ 0.028428999999999992, 0.03655800000000001, 0.08094000000000001, 0.161156, 0.317116, 0.5628799999999999, 1.0600879999999997, 1.1886799999999997, 1.863404, 2.3466249999999995, 2.935030000000001, 4.213820000000002, 5.129031000000001, 6.8124590000000005, 8.460858999999997, 10.153864000000004, 12.723004999999999, 14.690716999999998, 18.227418000000004, 21.245120999999997, 24.651687000000006, 29.15967400000001, 33.260406999999994, 36.764213, 42.314139, 46.17713800000001, 52.968818, 55.80477500000002, 62.42481499999999, 68.622887, 74.28433699999997, 83.803978, 84.13796699999999, 96.315509, 93.22745700000002, 107.306862, 110.113994, 118.93414999999999, 132.353638, 127.80191200000002, 136.713957, 142.79128799999992, 154.99034399999994, 161.55136399999995, 169.27909400000001, 178.14816499999998, 191.13649799999996, 195.84723399999996, 202.36205600000005, 213.98968999999997, 222.362937, 231.20247199999997, 242.02022599999992, 252.90685400000007, 263.39172299999996, 278.18651700000004, 293.90119500000003, 295.87100899999984, 317.33457200000004, 323.754392, 337.29555200000004, 352.34091099999983, 359.956823, 379.93912300000005, 396.688815, 430.60567599999996, 441.93988599999994, 449.00303099999996, 474.50754299999994, 478.0515210000001, 503.406317, 516.3476489999998, 526.496093, 549.4479789999998, 555.4682890000001, 579.4865380000001, 602.7906770000001, 611.400024, 625.9201740000001, 642.5213219999999, 665.1953820000001, 685.1941830400001, 693.6206259999998, 719.35359593, 728.57031682, 752.4430990599999, 775.0666659899999, 795.282943, 813.3700869900002, 821.513462, 855.9610939999999, 880.5235950000001, 894.4331140000002, 919.469816, 925.0669819999999, 949.8516299999997, 981.3070570000002, 992.5047240000001, 1021.2125579999998, 1035.2379919999998 ])  # Reemplaza ... con tus 100 valores de y

grado = 2
coeficientes = np.polyfit(x, y, grado)

polinomio = np.poly1d(coeficientes)

print("Función de ajuste:")
print(polinomio)

x_linea = np.linspace(min(x), max(x), 100)
y_linea = polinomio(x_linea)

plt.scatter(x, y, label='Datos originales')
plt.plot(x_linea, y_linea, color='red', label=f'Ajuste polinómico de grado {grado}')
plt.legend()
plt.xlabel('Gotículas')
plt.ylabel('Tiempo')
plt.title(f'Ajuste de tiempo de gotículas')
plt.show()

x = np.array([ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870])  # Reemplaza ... con tus 100 valores de x
y = np.array([ 14639, 97807, 307277, 693640, 1304833, 2212747, 3463608, 5100442, 7178317, 9772333, 12919347, 16679986, 21112764, 26265931, 32179239, 38928635, 46544382, 55126088, 64699364, 75292479, 86978018, 99864451, 113911102, 129214823, 145882887, 163871353, 183306867, 204225074, 226634327, 250681465, 276328340, 303707804, 332784780, 363682516, 396466745, 431080721, 467752353, 506346768, 547136859, 589891205, 634997320, 682193967, 731823352, 783645454, 837980851, 894706442, 953964274, 1015776357, 1080145696, 1147251309, 1216991545, 1289639030, 1364925955, 1443271408, 1524473643, 1608693225, 1695959926, 1786230022, 1879799888, 1976402269, 2076456136, 2179748785, 2286291557, 2396475143, 2509896413, 2627057326, 2747751917, 2871953362, 3000028646, 3131734781, 3267272168, 3406735614, 3549865926, 3697206279, 3848540315, 4003772694, 4163375739, 4327015938, 4494810014, 4667065068, 4843518683, 5024420207, 5209860693, 5399538267, 5594006763, 5793118257, 5996620445 ])

grado = 3
coeficientes = np.polyfit(x, y, grado)

polinomio = np.poly1d(coeficientes)

print("Función de ajuste:")
print(polinomio)

x_linea = np.linspace(min(x), max(x), 100)
y_linea = polinomio(x_linea)

plt.scatter(x, y, label='Datos originales')
plt.plot(x_linea, y_linea, color='red', label=f'Ajuste polinómico de grado {grado}')
plt.legend()
plt.xlabel('Gotículas')
plt.ylabel('Operaciones')
plt.title(f'Ajuste de operaciones de gotículas')
plt.show()