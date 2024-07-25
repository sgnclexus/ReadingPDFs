# from  pdfquery import PDFQuery

# pdf = PDFQuery('LIST_CAJ_200955.pdf')
# pdf.load()

# text_elements = pdf.pq('LTTextLineHorizontal')

# text = [t.text for t in text_elements]

# print(text)
import pandas as pd
import tabula

tables = tabula.read_pdf('LIST_CAJ_200955.pdf', pages='all', multiple_tables=True)
print('Tipo de dato: ',type(tables))
print('Longitud de tables: ',len(tables))
# df = tables[1]

i = 0
for table in tables:
    if table.columns.size != 8:
        tables.pop(i)        
    i += 1


df = pd.concat(tables)
df.to_csv('Tabla_Cajas_comipems.csv', encoding='utf-8')
print(df)