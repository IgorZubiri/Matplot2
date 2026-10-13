import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('precios_consolas.csv')
bataz_bestekoa = df[['Xbox', 'PS5', 'Switch', 'PC']].mean()
konsola_guztiak = ['Xbox', 'PS5', 'Switch', 'PC']
konsolak_alderatzeko = ['Xbox', 'PS5', 'Switch']
egun_kopurua = [(df['PC'] > df[k]).sum() for k in konsolak_alderatzeko]
merkeena = (
    df[konsola_guztiak].idxmin(axis=1).value_counts().reindex(konsola_guztiak)
)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
axes[0].bar(konsola_guztiak, bataz_bestekoa, color="steelblue")
axes[0].set_title("1. Bataz besteko prezioa €")
axes[0].set_ylabel("Prezioa €")
axes[1].bar(konsolak_alderatzeko, egun_kopurua, color="darkorange")
axes[1].set_title("2. Zenbat egunez den PC-a garestiagoa")
axes[1].set_xlabel("Kontsolak")
axes[1].set_ylabel("Egun kopurua")
axes[2].bar(merkeena.index, merkeena.values, color="seagreen")
axes[2].set_title("3. Zenbat egunez izan den kontsola merkeena")
axes[2].set_xlabel("Kontsola")
axes[2].set_ylabel("Egun kopurua")
plt.show()