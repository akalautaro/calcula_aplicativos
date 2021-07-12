import argparse
import os.path
from datetime import datetime


class Aplicativos:
    mes: int
    anio: int
    lotep: int
    jur: int
    filename_arba_p: str = ''
    filename_sicore: str = ''
    filename_sircar: str = ''
    filename_dreipo: str = ''
    filename_siager: str = ''
    base_dir: str = r'./'
    txt_in: str = r'./aplicativos'
    txt_out: str = r'./resultados'

    def __init__(self, mes: int, anio: int, lotep: int, jur: int):
        print(f"Mes a procesar {mes}\n")
        self.mes = mes
        self.anio = anio
        self.lotep = lotep
        self.jur = jur
        self.filename_arba_p = 'AR-alguien-{1}{0:0>2}0-7-LOTE{2:0>3}'.format(self.mes, self.anio, self.lotep)
        self.filename_siager_p = 'entre_rios_percepciones_a_clientes_alguien_{1}{0:0>2}'.format(self.mes, self.anio)
        self.filename_siager_r = 'entre_rios_retenciones_a_proveedores_alguien_{1}{0:0>2}'.format(self.mes, self.anio)
        self.filename_dreipo_p = 'dreipo_percepciones_alguien_{1}{0:0>2}'.format(self.mes, self.anio)
        self.filename_dreipo_r = 'dreipo_retenciones_alguien_{1}{0:0>2}'.format(self.mes, self.anio)
        self.filename_sircar_p = 'sicar_percepciones_a_clientes_{2}_alguien_{1}{0:0>2}_q0'.format(self.mes, self.anio, self.jur)
        self.filename_sircar_r = 'sicar_retenciones_a_proveedores_{2}_alguien_{1}{0:0>2}_q0'.format(self.mes, self.anio, self.jur)
        if not self.procesar_arba():
            print("No se proceso ARBA\n")
            pass
        if not self.procesar_siager():
            print("No se proceso SIAGER\n")
            pass
        if not self.procesar_dreipo():
            print("No se proceso DREIPO\n")
            pass
        if not self.procesar_sircar():
            print(f"No se proceso SIRCAR {jur}\n")
            pass

    def procesar_siager(self) -> bool:
        abs_fname_p: str = os.path.join(self.txt_in, self.filename_siager_p + '.txt')
        abs_fout_p: str = os.path.join(self.txt_out, f"Registros percepciones SIAGER {self.mes:0>2}{self.anio}" + '.txt')
        abs_fname_r: str = os.path.join(self.txt_in, self.filename_siager_r + '.txt')
        abs_fout_r: str = os.path.join(self.txt_out, f"Registros retenciones SIAGER {self.mes:0>2}{self.anio}" + '.txt')
        print(f"Procesando {abs_fname_p}")
        with open(abs_fname_p, 'r', encoding='utf-8') as f_p, open(abs_fout_p, 'w', encoding='utf-8') as f_out_p:
            importes = []
            for linea in f_p:
                linea_out = linea[65:80]
                linea_out = linea_out.replace(',', '.')
                importes.append(float(linea_out))

            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_p.write(f'Nro de registros: {nro_registros}\n')
            f_out_p.write(f'Importe: {str(importe_total)}')

            f_p.close()
            f_out_p.close()
        with open(abs_fname_r, 'r', encoding='utf-8') as f_r, open(abs_fout_r, 'w', encoding='utf-8') as f_out_r:
            importes = []
            for linea in f_r:
                linea_out = linea[90:102]
                linea_out = linea_out.replace(',', '.')
                importes.append(float(linea_out))

            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_r.write(f'Nro de registros: {nro_registros}\n')
            f_out_r.write(f'Importe: {str(importe_total)}')

            f_r.close()
            f_out_r.close()
        return True

    def procesar_sircar(self) -> bool:
        abs_fname_p: str = os.path.join(self.txt_in, self.filename_sircar_p + '.txt')
        abs_fout_p: str = os.path.join(self.txt_out,
                                       f"Registros percepciones SIRCAR {jur} {self.mes:0>2}{self.anio}" + '.txt')
        abs_fname_r: str = os.path.join(self.txt_in, self.filename_sircar_r + '.txt')
        abs_fout_r: str = os.path.join(self.txt_out,
                                       f"Registros retenciones SIRCAR {jur} {self.mes:0>2}{self.anio}" + '.txt')
        print(f"Procesando {abs_fname_p}")
        with open(abs_fname_p, 'r', encoding='utf-8') as f_p, open(abs_fout_p, 'w', encoding='utf-8') as f_out_p:
            importes = []
            lineas = f_p.readlines()
            for linea in lineas:
                linea_out = linea.split(',', -1)
                importes.append(float(linea_out[-3]))
            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_p.write(f'Nro de registros: {nro_registros}\n')
            f_out_p.write(f'Importe: {str(importe_total)}')
            print(importes)

            f_p.close()
            f_out_p.close()
        print(f"Procesando {abs_fname_r}")
        with open(abs_fname_r, 'r', encoding='utf-8') as f_r, open(abs_fout_r, 'w', encoding='utf-8') as f_out_r:
            importes = []
            lineas = f_r.readlines()
            for linea in lineas:
                linea_out = linea.split(',', -1)
                importes.append(float(linea_out[-3]))
            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_r.write(f'Nro de registros: {nro_registros}\n')
            f_out_r.write(f'Importe: {str(importe_total)}')

            f_r.close()
            f_out_r.close()
        return True

    def procesar_dreipo(self) -> bool:
        abs_fname_p: str = os.path.join(self.txt_in, self.filename_dreipo_p + '.txt')
        abs_fout_p: str = os.path.join(self.txt_out, f"Registros percepciones DREIPO {self.mes:0>2}{self.anio}" + '.txt')
        abs_fname_r: str = os.path.join(self.txt_in, self.filename_dreipo_r + '.txt')
        abs_fout_r: str = os.path.join(self.txt_out, f"Registros retenciones DREIPO {self.mes:0>2}{self.anio}" + '.txt')
        print(f"Procesando {abs_fname_p}")
        with open(abs_fname_p, 'r', encoding='utf-8') as f_p, open(abs_fout_p, 'w', encoding='utf-8') as f_out_p:
            importes = []
            lineas = f_p.readlines()[4:]
            for linea in lineas:
                linea_out = linea.split(';', -1)
                importes.append(float(linea_out[-1]))
            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_p.write(f'Nro de registros: {nro_registros}\n')
            f_out_p.write(f'Importe: {str(importe_total)}')

            f_p.close()
            f_out_p.close()
        print(f"Procesando {abs_fname_r}")
        with open(abs_fname_r, 'r', encoding='utf-8') as f_r, open(abs_fout_r, 'w', encoding='utf-8') as f_out_r:
            importes = []
            lineas = f_r.readlines()[4:]
            for linea in lineas:
                linea_out = linea.split(';', -1)
                importes.append(float(linea_out[-1]))
            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_r.write(f'Nro de registros: {nro_registros}\n')
            f_out_r.write(f'Importe: {str(importe_total)}')

            f_r.close()
            f_out_r.close()
        return True

    def procesar_arba(self) -> bool:
        abs_fname_p: str = os.path.join(self.txt_in, self.filename_arba_p + '.txt')
        abs_fout_p: str = os.path.join(self.txt_out, f"Registros percepciones ARBA {self.mes:0>2}{self.anio}" + '.txt')
        print(f"Procesando {abs_fname_p}")
        with open(abs_fname_p, 'r', encoding='utf-8') as f_p, open(abs_fout_p, 'w', encoding='utf-8') as f_out_p:
            importes = []
            for linea in f_p:
                linea_out = linea[38:46] + '\n'
                importes.append(float(linea_out))

            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_p.write(f'Nro de registros: {nro_registros}\n')
            f_out_p.write(f'Importe: {str(importe_total)}')

            f_p.close()
            f_out_p.close()
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Procesar aplicativos")
    parser.add_argument("--mes", help="mes del archivo a procesar", type=int)
    parser.add_argument("--anio", help="año del archivo a procesar", type=int)
    parser.add_argument("--lotep", help="lote percepciones ARBA", type=int)
    parser.add_argument("--jur", help="jurisdicción a procesar (906, 914)", type=int)
    args = parser.parse_args()
    mes: int = args.mes if args.mes else datetime.today().month
    anio: int = args.anio if args.anio else datetime.today().year
    lotep: int = args.lotep if args.lotep else 135
    jur: int = args.jur if args.jur else 906

    print("Parámetros mes: {0:0>2}, año: {1:d}".format(mes, anio))

    h = Aplicativos(mes, anio, lotep, jur)
