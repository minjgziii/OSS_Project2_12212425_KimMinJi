import pandas as pd

df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

print("#2-1  1)")

sectors = ['H', 'avg', 'HR', 'OBP']

for year in range(2015, 2019):
    print(f"[{year}] 각 부문별 상위 10명의 선수: ")

    for sector in sectors:
        df_year = df[df['year'] == year]
        df_sorted_year = df_year.sort_values(by=sector, ascending=False)
        top_players = df_sorted_year.head(10)

        print(f"{sector} 부문: ")
        print(top_players[['batter_name', sector]])
        print()

print("#2-1  2)")

positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
df_2018 = df[df['year'] == 2018]

print("[2018] 포지션별 승리 기여도(war)가 가장 높은 선수: ")

for position in positions:
    df_position = df_2018[df_2018['tp'] == position].sort_values('war', ascending=False)
    df_position['war_rank'] = df_position['war'].rank(ascending=False)
    highest_war_player = df_position[df_position['war_rank'] == 1]

    print(f"{position}: ")
    print(highest_war_player[['batter_name', 'war']])
    print()


print("#2-1  3)")

criterias = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
highest_correlation = -1
highest_correlation_criteria = None

for criteria in criterias:
    correlation = df['salary'].corr(df[criteria])

    if correlation > highest_correlation:
        highest_correlation = correlation
        highest_correlation_criteria = criteria

print(f"salary와 correlation이 가장 높은 지표: {highest_correlation_criteria}, correlation: {highest_correlation}")