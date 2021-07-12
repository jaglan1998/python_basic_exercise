# this program will calculate the base guide hours for wendy's
# i have made a dictionary using the excel inbuilt formula (="'"&A6&"':'"&B6&"', ")
# following data is extracted from excel, sales on LHS, Hours on RHS

import math

matrix = {
    '10000':'468.6',
    '10500':'473.9',
    '11000':'479.3',
    '11500':'484.5',
    '12000':'489.5',
    '12500':'494.3',
    '13000':'498.8',
    '13500':'503.4',
    '14000':'512.7',
    '14500':'520.3',
    '15000':'526.5',
    '15500':'532.3',
    '16000':'536.1',
    '16500':'540.9',
    '17000':'545.6',
    '17500':'549.3',
    '18000':'553.4',
    '18500':'556.6',
    '19000':'560.8',
    '19500':'564.6',
    '20000':'567.4',
    '20500':'572.7',
    '21000':'576.2',
    '21500':'580.2',
    '22000':'584.6',
    '22500':'587.7',
    '23000':'592.1',
    '23500':'595.8',
    '24000':'599.6',
    '24500':'604.3',
    '25000':'608.2',
    '25500':'612.7',
    '26000':'617.1',
    '26500':'621.2',
    '27000':'625.1',
    '27500':'629.9',
    '28000':'634.5',
    '28500':'638.9',
    '29000':'643.3',
    '29500':'647.9',
    '30000':'653.2',
    '30500':'657.3',
    '31000':'661.8',
    '31500':'667',
    '32000':'672',
    '32500':'675.7',
    '33000':'680.2',
    '33500':'685.1',
    '34000':'689.9',
    '34500':'694.1',
    '35000':'699.1',
    '35500':'703.3',
    '36000':'708.9',
    '36500':'712.9',
    '37000':'718.7',
    '37500':'722.5',
    '38000':'727.1',
    '38500':'732.2',
    '39000':'736.3',
    '39500':'739.8',
    '40000':'745',
    '40500':'748.4',
    '41000':'752.7',
    '41500':'757.8',
    '42000':'762.2',
    '42500':'766',
    '43000':'771.3',
    '43500':'776.1',
    '44000':'781.3',
    '44500':'785.9',
    '45000':'790.8',
    '45500':'794.6',
    '46000':'799.3',
    '46500':'804.5',
    '47000':'809.3',
    '47500':'813.1',
    '48000':'818.2',
    '48500':'822.7',
    '49000':'826.3',
    '49500':'832.1',
    '50000':'835.9',
    '50500':'839.7',
    '51000':'845.6',
    '51500':'849.2',
    '52000':'854.3',
    '52500':'858.9',
    '53000':'863.6',
    '53500':'868.2',
    '54000':'871.6',
    '54500':'876.5',
    '55000':'880.7',
    '55500':'885.5',
    '56000':'889.1',
    '56500':'894',
    '57000':'899.1',
    '57500':'903.7',
    '58000':'908.5',
    '58500':'911.9',
    '59000':'916.7',
    '59500':'921.9',
    '60000':'926.6',
    '60500':'931.4',
    '61000':'935.2',
    '61500':'939.9',
    '62000':'944.7',
    '62500':'949.3',
    '63000':'953',
    '63500':'958',
    '64000':'962.7',
    '64500':'967.2',
    '65000':'970.6',
    '65500':'975.1',
    '66000':'979.8',
    '66500':'983.2',
    '67000':'988.8',
    '67500':'991.9',
    '68000':'994.4',
    '68500':'997.3',
    '69000':'998.9',
    '69500':'1001.4',
    '70000':'1004.4',
    '70500':'1007.5',
    '71000':'1010.6',
    '71500':'1013.6',
    '72000':'1016.7',
    '72500':'1019.7',
    '73000':'1022.8',
    '73500':'1025.9',
    '74000':'1028.9',
    '74500':'1032',
    '75000':'1035.1',
    '75500':'1038.1',
    '76000':'1041.2',
    '76500':'1044.2',
    '77000':'1047.3',
    '77500':'1050.4',
    '78000':'1053.4',
    '78500':'1056.5',
    '79000':'1059.5',
    '79500':'1062.6',
    '80000':'1065.7',
    '80500':'1068.7',
    '81000':'1071.8',
    '81500':'1074.9',
    '82000':'1077.9',
    '82500':'1081',
    '83000':'1084',
    '83500':'1087.1',
    '84000':'1090.2',
    '84500':'1093.2',
    '85000':'1096.3',
    '85500':'1099.3',
    '86000':'1102.4',
    '86500':'1105.5',
    '87000':'1108.5',
    '87500':'1111.6',
    '88000':'1114.6',
    '88500':'1117.7',
    '89000':'1120.8',
    '89500':'1123.8',
    '90000':'1126.9',
    '90500':'1130',
    '91000':'1133',
    '91500':'1136.1',
    '92000':'1139.1',
    '92500':'1142.2',
    '93000':'1145.3',
    '93500':'1148.3',
    '94000':'1151.4',
    '94500':'1154.4',
    '95000':'1157.5',
    '95500':'1160.6',
    '96000':'1163.6',
    '96500':'1166.7',
    '97000':'1169.7',
    '97500':'1172.8',
    '98000':'1175.9',
    '98500':'1178.9',
    '99000':'1182',
    '99500':'1185.1',
    '100000':'1188.1'}

sales = round(float(input("Enter the sales: ")), 2)
ln_sales = round(float(input("Enter the late night sales: ")), 2)
lnh = round((191.7-(6500-math.ceil(7*ln_sales))/100)/7, 2)
print('LNH: ', lnh)

# print(sales, ln_sales)

# round down to the nearest 500
match_matrix = math.floor(round(((sales - ln_sales)*7), 2)/500)*500

found_matrix = None

for k,v in matrix.items():
    if int(k) == match_matrix:
        found_matrix = float(v)

bgh = round(found_matrix/7, 2)

print("BGH: ", bgh)


input("\n\nPress enter to exit the window......")




