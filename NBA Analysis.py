import pandas
import seaborn
import matplotlib.pyplot as plt

masters = pandas.read_csv("basketball_master.csv")
players = pandas.read_csv("basketball_players.csv")
nba = pandas.merge(players, masters, how="left", left_on="playerID", right_on="bioID")
cols = nba.columns
# mean = nba.points.mean()
median = nba.points.median()
max_points = nba[["playerID", "firstName", "lastName", "year", "points"]].sort_values("points", ascending=False).head(1)
data = players[["points", "assists", "rebounds"]]
# n.boxplot(data=data)
# plt.show()
mean = nba.points.mean()
group_years = players[["points", "year"]].groupby("year").median()
group_years = group_years.reset_index()
# seaborn.regplot(data=group_years, x="year", y="points")
# plt.show()
nba = nba[nba.points >= 1000]
nba = nba[nba.threeAttempted > 0]
nba["totalAttempts"] = nba["fgAttempted"] + nba["threeAttempted"] + nba["ftAttempted"]
nba['playerEffic'] = nba["points"] / nba["totalAttempts"]
effic = nba[["playerID", "firstName", "lastName", "points", "totalAttempts", "playerEffic"]].sort_values(
    "playerEffic", ascending=False).head(25)
# print(effic)
nba = nba[nba.steals > 0]
nba = nba[nba.threeMade > 0]
nba["exp_players"] = nba["rebounds"] + nba["assists"] + nba["steals"] + nba["fgMade"] + nba["threeMade"]
exp = nba[["lastName", "rebounds", "assists", "steals", "fgMade", "threeMade", "exp_players"]].sort_values(
    "exp_players", ascending=False).head(20)
# 2print(exp)
nba["goat"] = nba["fgMade"] + nba["threeMade"]
#goat = nba[["firstName", "lastName", "playerID", "year", "fgMade", "threeMade", "goat"]].sort_values("goat",
                                                                                                     #ascending=False).head(
    #25)

sum_goat = nba[["goat", "playerID"]].groupby("playerID").sum()
sum_goat = sum_goat.reset_index()
max_goat = sum_goat.sort_values("goat", ascending=False).head()
#print(goat)
#print(max_goat)
seaborn.barplot(x="playerID", y="goat",data=max_goat)
plt.show()

trend = nba[["threeMade", "year"]].groupby("year").sum()
trend = trend.reset_index()
#seaborn.pointplot(data=trend, x="year", y="threeMade")
#plt.show()

data_1 = nba[["firstName", "lastName", "hsState", "pos"]].head(60)



 print(data_1)
 seaborn.pointplot(data=trend, x="year", y="threeMade")

plt.show()
print(trend)
print(nba['playerEffic'])

plt.show()

