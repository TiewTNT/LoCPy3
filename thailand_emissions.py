import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('TKAgg')

plt.style.use('dark_background')

data = pd.read_csv('./thailand_co2_emission_1987_2022.csv')

ax1 = plt.subplot2grid(shape=(2, 6), loc=(0, 0), colspan=2)
ax2 = plt.subplot2grid(shape=(2, 6), loc=(0, 2), colspan=2)
ax3 = plt.subplot2grid(shape=(2, 6), loc=(0, 4), colspan=2)
ax4 = plt.subplot2grid(shape=(2, 6), loc=(1, 1), colspan=2)
ax5 = plt.subplot2grid(shape=(2, 6), loc=(1, 3), colspan=2)

ax1.plot(data.loc[data['source'] == 'industry'].groupby(['year']).agg('sum')['emissions_tons'], label='Industry')
ax1.set_xlabel('Year')
ax1.set_ylabel('CO₂ Emissions (tons)')

ax1.plot(data.loc[data['source'] == 'transport'].groupby(['year']).agg('sum')['emissions_tons'], label='Transport')

ax1.plot(data.loc[data['source'] == 'other'].groupby(['year']).agg('sum')['emissions_tons'], label='Other')

ax1.set_title('CO₂ Emissions (Year)')

ax_legend = ax1.legend()
for text in ax_legend.get_texts():
    text.set_fontsize(8)

ax2.pie(data.groupby('fuel_type').agg(count=('fuel_type', len))['count'], colors=['blue', '#0000cd', 'darkblue'], radius=3, center=(4, 4),
        wedgeprops={"linewidth": 3, "edgecolor": "black"}, frame=True, autopct='%1.1f%%')
ax2.legend(['Coal', 'Natural Gas', 'Oil'], loc='upper left', bbox_to_anchor=(-0.3, 1.1))

ax2.set_title('Fuel Type')

ax2.axis('off')

ax3.plot(data.groupby(['month']).agg('sum')['emissions_tons'])
ax3.set_title('CO₂ Emissions (Sum)')
ax3.set_xlabel('Month')
ax3.set_ylabel('CO₂ Emissions (tons)')
ax3.set_xticks(list(range(1, 13)))

ax4.plot(data.groupby(['year']).agg('sum'))

ax4.set_xlabel('Year')
ax4.set_ylabel('CO₂ Emissions (tons)')

ax4.set_title('Total Emissions')

ax5.set_title('Source')

ax5.pie(data.groupby('source').agg(count=('source', len))['count'], colors=['blue', '#0000cd', 'darkblue'], radius=3, center=(4, 4),
       wedgeprops={"linewidth": 3, "edgecolor": "black"}, frame=True, autopct='%1.1f%%')
ax5.legend(['Industry', 'Other', 'Transport'], loc='lower left', bbox_to_anchor=(0.8, -0.1))

ax5.axis('off')


plt.subplots_adjust(0.152)
suptitle = plt.suptitle('Thailand CO₂ Emissions (1987 - 2022)', fontsize=30)
suptitle.set_y(0.99)
plt.tight_layout()


manager = plt.get_current_fig_manager()
manager.resize(1000, 1000)

plt.subplots_adjust(left=0.05, right=0.98, top=0.9, bottom=0.06)
plt.show()
