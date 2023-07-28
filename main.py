# Include Libraries
import numpy as np
from fpdf import FPDF


# Eisagosi Dedomenwn (Onoma Arxeiou, Onoma simeiou, Apostasis anamesa sta dh)
def input_data(data_fileName):
    data = np.loadtxt(data_fileName, delimiter=' ', skiprows=0, dtype=str)

    return data

def org_data(raw_data, p_name, dh_data, dist_data, dh_name, n):

    for i in range(n):
        # add data to arrays from raw_data
        p_name.append(raw_data[i][0])
        dh_data[i] = raw_data[i][1]

        if raw_data.shape == (n,2):
            dist_data[i] = 1
        else:
            dist_data[i] = raw_data[i][2]

        # save the dh point to point for the calc of A array
        tmp = p_name[i]
        a = tmp.split('-', 1)
        dh_name.append(a)
    return 0


def create_A(A, dh_name, n, m, dh_codes, stahero):

    dh_codes_ = np.delete(dh_codes, np.where(dh_codes == stahero))

    for i in range(n):
        for j in range(m):
            a = dh_name[i][0]
            b = dh_name[i][1]

            if dh_codes_[j] == a:
                A[i, j] = -1
            if dh_codes_[j] == b:
                A[i, j] = 1

    return A

def create_P(P, dist_data):
    for i in range(n):
        P[i, i] = 1 / dist_data[i, 0]

    return P

def create_dl(L, dl, dh_name, H_0, dh_codes, stahero):

    for i in range(n):
        a = dh_name[i][0]
        b = dh_name[i][1]

        if a == stahero:
            dl[i ,0] = L[i, 0] + H_0
        if b == stahero:
            dl[i, 0] = L[i, 0] - H_0
        if a != stahero and b != stahero:
            dl[i, 0] = L[i, 0]

    return dl


def calc_errors(errors, Vx, m):

    for i in range(m):
        errors[i, 0] = np.sqrt(Vx[i,i])

    return errors


def report_txt(x, errors, s_0, H_0, dh_codes, m):

    dh_codes_ = np.delete(dh_codes, np.where(dh_codes == stahero))

    with open('report.txt', 'w') as f:
        tmp = ['Hi ', 'Value(m) ', 'Error(m)']
        f.writelines(tmp)
        f.writelines('\n')
        f.writelines('\n')
        pdf.set_font("Helvetica", style='u', size=11.5)
        pdf.cell(0, 10, txt='Hi    '+ 'Value(m)    '+ 'Error(m)', border=0, ln=2, align='L')
        pdf.set_font("Helvetica", size=11)


        for i in range(m):
            tmp = [str(dh_codes_[i]), ' ' , str(round(x[i, 0], 3)), ' ' ,str(round(errors[i, 0], 4))]
            f.writelines(tmp)
            f.writelines('\n')
            text = str(str(dh_codes_[i]) + '    ' + str(round(x[i, 0], 3)) + '    +-' + str(round(errors[i, 0], 4)))
            pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

        tmp = [str(stahero), ' ' , str(H_0), ' ' , str(0)]
        f.writelines(tmp)
        f.writelines('\n')
        f.writelines('\n')

        tmp = ['s_0 ', str(round(s_0[0,0], 4)), ' m']
        f.writelines(tmp)

        text = str(str(stahero) + '    ' + str(H_0) + '    ' + str(0))
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

        text = str('s_0   ' + str(round(s_0[0,0], 4)) + ' m')
        pdf.cell(0, 10, txt=text, border=0, ln=2, align='L')

    with open('output.txt', 'w') as f:
        for i in range(m):
            tmp = [str(round(x[i, 0], 3))]
            f.writelines(tmp)
            f.writelines('\n')
        f.writelines(str(H_0))

    return 0


def print_u_in_pdf(u, dh_name):

    pdf.set_font("Helvetica", style='u', size=11.5)
    pdf.cell(0, 6, txt='Ypoloipa (mm)', border=0, ln=2, align='L')
    pdf.set_font("Helvetica", size=11)


    for i in range(len(u)):
        text = str(str(dh_name[i][1]) + ' - ' + str(dh_name[i][0]) + '  ' + str(round(u[i][0]*1000, 1)))
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')


    return 0


if __name__ == "__main__":
    data_file_name = "C:\\Users\\nikos\\OneDrive\\Files\\Projectakia\\Geodesy_Projects\\Dedomena\\Yhometriko_Diktio\\demo_data.txt"

    # Apothikeusi output se ena arxeio pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, txt='Apotelsmta Synorthosis Yhometrikou Diktiou', border=1, ln=2, align='C')
    pdf.set_font("Helvetica", size=11)

    # input raw data from txt file
    raw_data = input_data(data_file_name)

    # get number of observations
    n = len(raw_data)

    # define arrays for data
    p_name = []
    dh_data = np.zeros((n, 1))
    dist_data = np.zeros((n, 1))
    dh_name = []

    # organaze data to arrays for point name, dh and distance
    org_data(raw_data, p_name, dh_data, dist_data, dh_name, n)

    # least squares solve
    k =  len(np.unique(dh_name))  # number of points (or input from user)
    m = k - 1
    H_0 = 180.369#100.000 # meters
    stahero = 'r2'

    # arrays for A*x = dl + u solve
    P = np.zeros((n, n))
    A = np.zeros((n, m))
    L = dh_data
    dl = np.zeros((n , 1))
    errors = np.zeros((m, 1))
    dh_codes = np.array(np.unique(dh_name))

    # generation of arrays from data
    create_P(P, dist_data)

    create_A(A, dh_name, n, m, dh_codes, stahero)

    create_dl(L, dl, dh_name, H_0, dh_codes, stahero)

    # calc of x array
    N = np.transpose(A)@P@A
    x = np.linalg.inv(N)@np.transpose(A)@P@dl
    u = A@x - dl
    s_0 = np.sqrt( np.transpose(u)@P@u/(n - m) )
    Vx = (s_0**2)*np.linalg.inv(N)

    calc_errors(errors, Vx, m)

    report_txt(x, errors, s_0, H_0, dh_codes, m)

    print_u_in_pdf(u, dh_name)

    pdf.output("Apotelesmta_Analytika.pdf")


    #print(u)
