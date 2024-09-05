def utama():
    beri_salam()
    status_pasangan = dapatkan_input("Dah ada pasangan/calon? (ya/tidak): ")

    if status_pasangan == "ya":
        tamatkan_perbualan("Saya berhenti di sini sahaja dan tidak akan berhubung tanpa urusan.")
    elif status_pasangan == "tidak":
        teruskan_taaruf()
    else:
        pilihan_tidak_sah()

def beri_salam():
    print("Assalamualaikum")
    print("Tujuan saya mesej ini hanya untuk bertanya status cik?")

def dapatkan_input(arahan):
    return input(arahan).strip().lower()

def tamatkan_perbualan(pesan):
    print(pesan)

def teruskan_taaruf():
    status_taaruf = dapatkan_input("Sudi untuk bertaaruf? (ya/tidak): ")
    
    if status_taaruf == "ya":
        print("InsyaAllah kita boleh berbincang untuk urusan seterusnya. Jika rasa tidak sesuai/serasi, boleh hentikan taaruf.")
    elif status_taaruf == "tidak":
        tamatkan_perbualan("Saya berhenti di sini sahaja dan tidak akan berhubung tanpa urusan.")
    else:
        pilihan_tidak_sah()

def pilihan_tidak_sah():
    print("Pilihan tidak sah.")

if __name__ == "__main__":
    utama()
