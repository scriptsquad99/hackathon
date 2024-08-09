import pandas as pd
from matplotlib import pyplot as plt

def saveFile(df):
    df = pd.to_csv(r'C:\Users\drtam\Downloads\Tamanna\Data.csv')
def createDf():
    df = pd.DataFrame(
        {
            'Day': ['Monday','Tuesday','Wednesday','Thursday','Friday'],
            'Time': ['1 Hr','2 Hr','3 Hr','4 Hr','5 Hr']
        }
    )
    return df
    if __name__=='__main':
        df = createDf()
        saveFile(df)
        pd.read_csv(r'C:\Users\drtam\Downloads\Tamanna\Data.csv')
        print(df)
        plt.rcParams.update({'font.size': 20})
        fig, ax = plt.subplot(figsize=(7.3,6.3))
        df.plot(ax=ax,kind='pi',x='Day',y='Time',color='red')
        ax.tick_params(axis='x',labelrotation=0)
        fig.suptitle(t='Exercise Timings Per Day',fontsize=25)
        plt.savefig(r'C:\Users\drtam\Downloads\Tamanna\plot.png')
