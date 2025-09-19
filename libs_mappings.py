# --- Dimensione Economica ---
scoring_economica = {
    "Nessuna creazione misurabile di posti di lavoro o ruoli esclusivamente a breve termine/precari; salari inferiori agli standard locali; nessun stimolo economico": 1,
    "Creazione limitata di posti di lavoro con stabilità minima; ruoli per lo più part-time o insicuri; debole collegamento con l'attività economica locale.": 2,
    "Occupazione stabile per alcuni gruppi target; salari e contratti equi; contributo moderato alla circolazione economica locale.": 3,
    "Creazione significativa e sostenuta di posti di lavoro con paga equa e benefici in regioni svantaggiate o gruppi marginalizzati; rafforza le catene di approvvigionamento locali.": 4,
    "Crea occupazione di alta qualità e sicura su larga scala; promuove un cambiamento strutturale nel mercato del lavoro locale o modelli economici inclusivi; dimostra un valore a lungo termine oltre il ciclo del progetto.": 5
}

# --- Dimensione Salute ---
scoring_salute = {
    "Nessun miglioramento misurabile; possibili segni di ulteriore degrado.": 1,
    "Condizioni dell'ecosistema mantenute; lievi miglioramenti evidenti.": 2,
    "Miglioramento evidente in uno o più parametri ecosistemici. Segni iniziali di recupero, ma limitati in scala o portata.": 3,
    "Ripristino raggiunto; cambiamento positivo in molteplici parametri ecosistemici come biodiversità, salute del suolo o struttura dell'habitat.": 4,
    "Rigenerazione sistemica; ripristino della connettività, biodiversità e sostenibilità a lungo termine.": 5
}

# --- Dimensione Ambientale - Emissioni ---
scoring_ambientale_emissioni = {
    "Nessuna riduzione misurabile; possibili aumenti delle emissioni. <1 tonnellata di CO2 rimossa": 1,
    "Riduzioni minime o marginali rispetto alla baseline. 1-10 tonnellate di CO2 rimosse": 2,
    "Riduzione evidente ma limitata in scala o impatto. 10-50 tonnellate di CO2 rimosse, tracciabilità e addizionalità moderate.": 3,
    "Riduzione significativa e sostenuta delle emissioni in uno o più settori o attività. 50-100 tonnellate di CO2 rimosse; dati solidi e sequestro durevole.": 4,
    "Riduzione sistemica e duratura delle emissioni con impatti a livello territoriale o settoriale, contribuendo in modo rilevante agli obiettivi climatici a lungo termine. 100 tonnellate di CO2 rimosse; alta permanenza, scalabilità e contributo positivo al clima.": 5
}


# --- Dimensione Ambientale - Rifiuti ---
scoring_ambientale_rifiuti = {
    "<20% dei rifiuti gestiti in modo sostenibile.": 1,
    "20-39% gestiti in modo sostenibile.": 2,
    "40-59% gestiti in modo sostenibile.": 3,
    "60-79% gestiti in modo sostenibile.": 4,
    "≥80% dei rifiuti gestiti in modo sostenibile, con soluzioni circolari integrate.": 5
}

# --- Dimensione Tecnologica ---
scoring_tecnologica = {
    "Adattamento minimo di tecnologie esistenti; nessuna adozione o diffusione esterna.": 1,
    "Certa novità, limitata all'uso interno; partnership locali o replicazioni minori.": 2,
    "Innovazione o trasferimento moderato; adottato da almeno un partner esterno o replicato una volta.": 3,
    "Innovazione o diffusione sostanziale; adottato da più attori esterni o formalizzato nell'uso pubblico.": 4,
    "Trasferimento sistemico; scalato a livello regionale o nazionale; contribuisce agli ecosistemi di innovazione aperta.": 5
}

# --- Dimensione Sociale e Diritti Civili (Equità) ---
scoring_sociale_equita = {
    "Nessun cambiamento osservabile; le disuguaglianze persistono o c'è un leggero aumento potenziale.": 1,
    "Miglioramenti minori per una popolazione o ambito limitato.": 2,
    "Riduzione misurabile delle disuguaglianze tra i gruppi target; ridotti i divari di accesso.": 3,
    "Miglioramenti ampi e sostenuti nell'equità tra più gruppi.": 4,
    "Cambiamento strutturale nella distribuzione dell'equità; i gruppi vulnerabili ottengono accesso o controllo sistemico sulle risorse.": 5
}

# --- Dimensione Sociale e Diritti Civili (Lavoro) ---
scoring_sociale_lavoro = {
    "Conformità parziale agli standard di base; protezione minima o applicazione debole.": 1,
    "Protezioni di base per i lavoratori presenti.": 2, 
    "Applicazione coerente di pratiche lavorative eque, inclusi salario minimo, orari ragionevoli e condizioni sicure; alcune lacune nella contrattazione collettiva o nella stabilità a lungo termine.": 3,
    "Forte conformità agli standard internazionali; lavoro dignitoso e contratti stabili.": 4,
    "Ambiente di lavoro esemplare; promuove equità, diritti collettivi, protezione sociale e mobilità sociale verso l'alto.": 5
}


# --- Dimensione Istituzionale (Governance) ---
scoring_istituzionale_governance = {
    "Nessun quadro formale di governance o infrastruttura etica in atto.": 1,
    "Strutture etiche o di responsabilità parziali; politiche deboli o non applicate.": 2,
    "Esistenza di politiche formali; certa conformità e consapevolezza del personale, applicazione limitata.": 3,
    "Modello di governance chiaro; applicazione attiva; canali etici accessibili.": 4,
    "Struttura di governance completamente trasparente e partecipativa con forte responsabilità, meccanismi di rendicontazione e feedback.": 5
}

# --- Dimensione Istituzionale (Stakeholder) ---
scoring_istituzionale_stakeholder = {
    "Nessun coinvolgimento degli stakeholder o partecipazione puramente simbolica.": 1,
    "Consultazioni limitate; gruppi selezionati invitati ma con bassa influenza.": 2,
    "Partecipazione degli stakeholder presente nelle fasi di pianificazione o revisione; qualche influenza.": 3,
    "Stakeholder attivamente coinvolti durante tutto il processo; implementazione di processi di co-progettazione.": 4,
    "Modello completo di co-governance con condivisione del potere e collaborazione duratura tra i settori.": 5
}

# --- Dimensione Territoriale ---
scoring_territoriale = {
    "Nessun coinvolgimento della comunità o sfiducia; attività scollegate dai bisogni locali.": 1,
    "Coinvolgimento limitato o simbolico; partecipazione di un gruppo demografico ristretto.": 2,
    "Coinvolgimento regolare di alcuni membri della comunità; fiducia e dialogo moderati.": 3,
    "Ampia partecipazione di gruppi locali diversi; alta visibilità e accettazione.": 4,
    "Coinvolgimento profondo, duraturo e co-creativo tra i settori; forte senso di appartenenza locale e coesione sociale.": 5
}

# --- Dimensione Educativa, Culturale e Cognitiva ---
scoring_educativa = {
    "Nessuna formazione o formazione simbolica; aspetti culturali/educativi assenti.": 1,
    "Sforzi formativi sporadici o basilari con partecipazione limitata.": 2,
    "Eventi di apprendimento regolari; diversità moderata di partecipanti o contenuti.": 3,
    "Attività educative multidisciplinari e inclusive; coinvolgimento continuo.": 4,
    "Programmazione educativa e culturale istituzionalizzata, radicata nelle strutture pubbliche o comunitarie.": 5
}

# --- Dimensione Generazionale ---
scoring_generazionale = {
    "Nessun coinvolgimento dei giovani o pianificazione orientata al futuro.": 1,
    "Riferimenti minimi agli obiettivi a lungo termine; coinvolgimento simbolico dei giovani.": 2,
    "Partecipazione attiva di alcuni giovani e considerazioni esplicite sul futuro.": 3,
    "I giovani sono regolarmente coinvolti; i benefici a lungo termine sono chiaramente progettati.": 4,
    "Ruoli di leadership e governance giovanile; pianificazione focalizzata sul futuro integrata nella strategia principale.": 5
}
