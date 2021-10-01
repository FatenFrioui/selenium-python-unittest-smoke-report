# import pandas as pd
#
# # combiner 3 fichiers
# fichiers=['C:\Users\Faten\Desktop\manuel_test\cas_test_authentification.xlsx','C:\Users\Faten\Desktop\manuel_test\cas_test_authentification2.xlsx','C:\Users\Faten\Desktop\manuel_test\cas_test_authentification3.xlsx']
# # créer le fichier combiné de type dataframe
# fichier_combine=pd.DataFrame()
# # combine les 3 fichiers
# for fichier in fichiers:
#     df=pd.read_excel(fichier,skiprows=3)
#     print(df)
#     fichier_combine=fichier_combine.append(df,ignore_index=True)
#     # créer le fichier excel correspondant
# fichier_combine.to_excel('fichier_comb.xlsx')
