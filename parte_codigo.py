 """for i in N:
            #print(i, aux)
            if(i=='0'):
                print(i)
                aux2.append(i)

            else:
                print(i)
                print(N_Factura)
                aux2.append(str(N_Factura))
                break"""

        #aux2=''.join(aux2)

    
     excel_doc=openpyxl.Workbook()
        hoja=excel_doc.active
        print(f'Hoja activa: {hoja.title}')

        hoja.title="factura"

        print(f'{excel_doc.active.title}')

        hoja["A1"]="nombre"
        a1=hoja["A1"]
        print(a1.value)

        a2=hoja.cell(row=1, column=2, value=20)
        print(a2.value)

        fila=["","","",""]


        #para abrir el archivo excel
        #excel_doc=openpyxl.load_workbook('juan.xlsx')
        #para saber los nombres de las hojas de el libro
        #N=excel_doc.get_sheet_names()
        #para escojer una hoja en expecifico
        #hoja=excel_doc.get_sheet_by_name('Hoja1')
        #print(N,hoja)

        #hoja2=excel_doc.copy_worksheet(hoja)

         #excel_doc.save()

        #print(hoja['G9'].value)