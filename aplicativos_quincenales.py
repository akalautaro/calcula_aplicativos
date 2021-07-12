import argparse
import os.path
from datetime import datetime


class Aplicativos:
    mes: int
    anio: int
    loter: int
    quincena: int
    filename_arba_r: str = ''
    filename_sircar: str = ''
    filename_sicore: str = ''
    base_dir: str = r'./'
    txt_in: str = r'./aplicativos'
    txt_out: str = r'./resultados'

    def __init__(self, mes: int, anio: int, loter: int, jur: int, quincena: int):
        print(f"Mes a procesar {mes}\n")
        self.mes = mes
        self.anio = anio
        self.loter = loter
        self.jur = jur
        self.quincena = quincena
        self.filename_arba_r = 'AR-alguien-{1}{0:0>2}1-6-LOTE{2:0>3}'.format(self.mes, self.anio, self.loter)
        self.filename_sicore = 'sicore_q{2}_alguien_{1}{0:0>2}'.format(self.mes, self.anio, self.quincena)
        self.filename_sircar_p = 'sicar_percepciones_a_clientes_921_alguien_{1}{0:0>2}_q{2}'.format(self.mes, self.anio, self.quincena)
        self.filename_sircar_r = 'sicar_retenciones_921_alguien_{1}{0:0>2}_q{2}'.format(self.mes, self.anio, self.quincena)
        if not self.procesar_arba():
            print("No se proceso ARBA\n")
            pass
        if not self.procesar_sicore():
            print("No se proceso SICORE\n")
            pass
        if not self.procesar_sircar():
            print(f"No se proceso SIRCAR {jur}\n")
            pass

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
            # print(importes)
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

    def procesar_sicore(self) -> bool:
        abs_fname: str = os.path.join(self.txt_in, self.filename_sicore + '.txt')
        abs_fout: str = os.path.join(self.txt_out, f"Registros SICORE {self.mes:0>2}{self.anio} q{self.quincena}" + '.txt')
        print(f"Procesando {abs_fname}")
        with open(abs_fname, 'r', encoding='utf-8') as f_p, open(abs_fout, 'w', encoding='utf-8') as f_out_p:
            importes = []
            for linea in f_p:
                linea_out = linea[78:93] + '\n'
                linea_out = linea_out.replace(',', '.')
                linea_out = linea_out.replace(' ', '0')
                importes.append(float(linea_out))

            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_p.write(f'Nro de registros: {nro_registros}\n')
            f_out_p.write(f'Importe: {str(importe_total)}')

            f_p.close()
            f_out_p.close()
        return True

    def procesar_arba(self) -> bool:
        abs_fname_r: str = os.path.join(self.txt_in, self.filename_arba_r + '.txt')
        abs_fout_r: str = os.path.join(self.txt_out, f"Registros retenciones ARBA {self.mes:0>2}{self.anio}" + '.txt')
        print(f"Procesando {abs_fname_r}")
        with open(abs_fname_r, 'r', encoding='utf-8') as f_r, open(abs_fout_r, 'w', encoding='utf-8') as f_out_r:
            importes = []
            for linea in f_r:
                linea_out = linea[38:46] + '\n'
                importes.append(float(linea_out))

            importe_total = round(sum(importes), 2)
            nro_registros = len(importes)
            f_out_r.write(f'Nro de registros: {nro_registros}\n')
            f_out_r.write(f'Importe: {str(importe_total)}')

            f_r.close()
            f_out_r.close()
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Procesar aplicativos")
    parser.add_argument("--mes", help="mes del archivo a procesar", type=int)
    parser.add_argument("--anio", help="año del archivo a procesar", type=int)
    parser.add_argument("--loter", help="lote retenciones ARBA", type=int)
    parser.add_argument("--jur", help="jurisdicción a procesar (por defecto 921)", type=int)
    parser.add_argument("--quincena", help="quincena (0 mes entero)", type=int)
    args = parser.parse_args()
    mes: int = args.mes if args.mes else datetime.today().month
    anio: int = args.anio if args.anio else datetime.today().year
    loter: int = args.loter if args.loter else 192
    jur: int = args.jur if args.jur else 921
    quincena: int = args.quincena if args.quincena else 0

    print("Parámetros mes: {0:0>2}, año: {1:d}".format(mes, anio))

    h = Aplicativos(mes, anio, loter, jur, quincena)
