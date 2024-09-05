def main():
    greet_user()
    pasangan_status = get_user_input("Dah ada pasangan/calon? (ya/tidak): ")

    if pasangan_status == "ya":
        end_conversation("Saya berhenti di sini sahaja dan tidak akan berhubung tanpa urusan.")
    elif pasangan_status == "tidak":
        proceed_taaruf()
    else:
        invalid_choice()

def greet_user():
    print("Assalamualaikum")
    print("Tujuan saya mesej ini hanya untuk bertanya status cik Anis")

def get_user_input(prompt):
    return input(prompt).strip().lower()

def end_conversation(message):
    print(message)

def proceed_taaruf():
    taaruf_status = get_user_input("Sudi untuk bertaaruf? (ya/tidak): ")
    
    if taaruf_status == "ya":
        print("InsyaAllah boleh berbincang untuk urusan seterusnya. Jika rasa tidak sesuai/serasi, boleh hentikan taaruf.")
    elif taaruf_status == "tidak":
        end_conversation("Saya berhenti di sini sahaja dan tidak akan berhubung tanpa urusan.")
    else:
        invalid_choice()

def invalid_choice():
    print("Pilihan tidak sah.")

if __name__ == "__main__":
    main()
