from django.utils.translation import ugettext_lazy as _


ORDER_STATUS = (
    ("Draft", "Draft"),
    ("Sent", "Sent"),
    ("Paid", "Paid"),
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancel"),
)




CURRENCY_CODES = (
    ("AED", _("AED, Dirham")),
    ("AFN", _("AFN, Afghani")),
    ("ALL", _("ALL, Lek")),
    ("AMD", _("AMD, Dram")),
    ("ANG", _("ANG, Guilder")),
    ("AOA", _("AOA, Kwanza")),
    ("ARS", _("ARS, Peso")),
    ("AUD", _("AUD, Dollar")),
    ("AWG", _("AWG, Guilder")),
    ("AZN", _("AZN, Manat")),
    ("BAM", _("BAM, Marka")),
    ("BBD", _("BBD, Dollar")),
    ("BDT", _("BDT, Taka")),
    ("BGN", _("BGN, Lev")),
    ("BHD", _("BHD, Dinar")),
    ("BIF", _("BIF, Franc")),
    ("BMD", _("BMD, Dollar")),
    ("BND", _("BND, Dollar")),
    ("BOB", _("BOB, Boliviano")),
    ("BRL", _("BRL, Real")),
    ("BSD", _("BSD, Dollar")),
    ("BTN", _("BTN, Ngultrum")),
    ("BWP", _("BWP, Pula")),
    ("BYR", _("BYR, Ruble")),
    ("BZD", _("BZD, Dollar")),
    ("CAD", _("CAD, Dollar")),
    ("CDF", _("CDF, Franc")),
    ("CHF", _("CHF, Franc")),
    ("CLP", _("CLP, Peso")),
    ("CNY", _("CNY, Yuan Renminbi")),
    ("COP", _("COP, Peso")),
    ("CRC", _("CRC, Colon")),
    ("CUP", _("CUP, Peso")),
    ("CVE", _("CVE, Escudo")),
    ("CZK", _("CZK, Koruna")),
    ("DJF", _("DJF, Franc")),
    ("DKK", _("DKK, Krone")),
    ("DOP", _("DOP, Peso")),
    ("DZD", _("DZD, Dinar")),
    ("EGP", _("EGP, Pound")),
    ("ERN", _("ERN, Nakfa")),
    ("ETB", _("ETB, Birr")),
    ("EUR", _("EUR, Euro")),
    ("FJD", _("FJD, Dollar")),
    ("FKP", _("FKP, Pound")),
    ("GBP", _("GBP, Pound")),
    ("GEL", _("GEL, Lari")),
    ("GHS", _("GHS, Cedi")),
    ("GIP", _("GIP, Pound")),
    ("GMD", _("GMD, Dalasi")),
    ("GNF", _("GNF, Franc")),
    ("GTQ", _("GTQ, Quetzal")),
    ("GYD", _("GYD, Dollar")),
    ("HKD", _("HKD, Dollar")),
    ("HNL", _("HNL, Lempira")),
    ("HRK", _("HRK, Kuna")),
    ("HTG", _("HTG, Gourde")),
    ("HUF", _("HUF, Forint")),
    ("IDR", _("IDR, Rupiah")),
    ("ILS", _("ILS, Shekel")),
    ("INR", _("INR, Rupee")),
    ("IQD", _("IQD, Dinar")),
    ("IRR", _("IRR, Rial")),
    ("ISK", _("ISK, Krona")),
    ("JMD", _("JMD, Dollar")),
    ("JOD", _("JOD, Dinar")),
    ("JPY", _("JPY, Yen")),
    ("KES", _("KES, Shilling")),
    ("KGS", _("KGS, Som")),
    ("KHR", _("KHR, Riels")),
    ("KMF", _("KMF, Franc")),
    ("KPW", _("KPW, Won")),
    ("KRW", _("KRW, Won")),
    ("KWD", _("KWD, Dinar")),
    ("KYD", _("KYD, Dollar")),
    ("KZT", _("KZT, Tenge")),
    ("LAK", _("LAK, Kip")),
    ("LBP", _("LBP, Pound")),
    ("LKR", _("LKR, Rupee")),
    ("LRD", _("LRD, Dollar")),
    ("LSL", _("LSL, Loti")),
    ("LTL", _("LTL, Litas")),
    ("LVL", _("LVL, Lat")),
    ("LYD", _("LYD, Dinar")),
    ("MAD", _("MAD, Dirham")),
    ("MDL", _("MDL, Leu")),
    ("MGA", _("MGA, Ariary")),
    ("MKD", _("MKD, Denar")),
    ("MMK", _("MMK, Kyat")),
    ("MNT", _("MNT, Tugrik")),
    ("MOP", _("MOP, Pataca")),
    ("MRO", _("MRO, Ouguiya")),
    ("MUR", _("MUR, Rupee")),
    ("MVR", _("MVR, Rufiyaa")),
    ("MWK", _("MWK, Kwacha")),
    ("MXN", _("MXN, Peso")),
    ("MYR", _("MYR, Ringgit")),
    ("MZN", _("MZN, Metical")),
    ("NAD", _("NAD, Dollar")),
    ("NGN", _("NGN, Naira")),
    ("NIO", _("NIO, Cordoba")),
    ("NOK", _("NOK, Krone")),
    ("NPR", _("NPR, Rupee")),
    ("NZD", _("NZD, Dollar")),
    ("OMR", _("OMR, Rial")),
    ("PAB", _("PAB, Balboa")),
    ("PEN", _("PEN, Sol")),
    ("PGK", _("PGK, Kina")),
    ("PHP", _("PHP, Peso")),
    ("PKR", _("PKR, Rupee")),
    ("PLN", _("PLN, Zloty")),
    ("PYG", _("PYG, Guarani")),
    ("QAR", _("QAR, Rial")),
    ("RON", _("RON, Leu")),
    ("RSD", _("RSD, Dinar")),
    ("RUB", _("RUB, Ruble")),
    ("RWF", _("RWF, Franc")),
    ("SAR", _("SAR, Rial")),
    ("SBD", _("SBD, Dollar")),
    ("SCR", _("SCR, Rupee")),
    ("SDG", _("SDG, Pound")),
    ("SEK", _("SEK, Krona")),
    ("SGD", _("SGD, Dollar")),
    ("SHP", _("SHP, Pound")),
    ("SLL", _("SLL, Leone")),
    ("SOS", _("SOS, Shilling")),
    ("SRD", _("SRD, Dollar")),
    ("SSP", _("SSP, Pound")),
    ("STD", _("STD, Dobra")),
    ("SYP", _("SYP, Pound")),
    ("SZL", _("SZL, Lilangeni")),
    ("THB", _("THB, Baht")),
    ("TJS", _("TJS, Somoni")),
    ("TMT", _("TMT, Manat")),
    ("TND", _("TND, Dinar")),
    ("TOP", _("TOP, Paanga")),
    ("TRY", _("TRY, Lira")),
    ("TTD", _("TTD, Dollar")),
    ("TWD", _("TWD, Dollar")),
    ("TZS", _("TZS, Shilling")),
    ("UAH", _("UAH, Hryvnia")),
    ("UGX", _("UGX, Shilling")),
    ("USD", _("$, Dollar")),
    ("UYU", _("UYU, Peso")),
    ("UZS", _("UZS, Som")),
    ("VEF", _("VEF, Bolivar")),
    ("VND", _("VND, Dong")),
    ("VUV", _("VUV, Vatu")),
    ("WST", _("WST, Tala")),
    ("XAF", _("XAF, Franc")),
    ("XCD", _("XCD, Dollar")),
    ("XOF", _("XOF, Franc")),
    ("XPF", _("XPF, Franc")),
    ("YER", _("YER, Rial")),
    ("ZAR", _("ZAR, Rand")),
    ("ZMK", _("ZMK, Kwacha")),
    ("ZWL", _("ZWL, Dollar")),
)