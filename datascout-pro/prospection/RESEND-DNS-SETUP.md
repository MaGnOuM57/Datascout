# Resend DNS Setup - Configuration Anti-Spam

## Étape 1: Ajouter le domaine dans Resend

1. Va sur https://resend.com/domains
2. Clique "Add Domain"
3. Entre: `datascout.pro`
4. Resend va générer 3 DNS records

---

## Étape 2: Configurer DNS chez ton registrar

**Tu vas recevoir 3 types de records:**

### 1. SPF (Sender Policy Framework)
```
Type: TXT
Name: @
Value: v=spf1 include:resend.com ~all
```

### 2. DKIM (DomainKeys Identified Mail)
```
Type: TXT
Name: resend._domainkey
Value: [une longue clé cryptée fournie par Resend]
```

### 3. DMARC (Domain-based Message Authentication)
```
Type: TXT
Name: _dmarc
Value: v=DMARC1; p=none; rua=mailto:contact@datascout.pro
```

---

## Étape 3: Ajouter DMARC renforcé (IMPORTANT pour délivrabilité)

**Ajoute ce record en PLUS de celui de Resend:**

```
Type: TXT
Name: _dmarc.datascout.pro
Value: v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@datascout.pro; ruf=mailto:dmarc-forensics@datascout.pro; pct=100; adkim=s; aspf=s
```

**Explication:**
- `p=quarantine`: Les emails suspects vont en spam (vs `reject` qui delete)
- `rua`: Rapports agrégés quotidiens
- `adkim=s`: Strict DKIM alignment
- `aspf=s`: Strict SPF alignment

---

## Étape 4: Vérifier propagation DNS (5-30 min)

```bash
# Check SPF
dig TXT datascout.pro +short

# Check DKIM
dig TXT resend._domainkey.datascout.pro +short

# Check DMARC
dig TXT _dmarc.datascout.pro +short
```

---

## Étape 5: Vérifier dans Resend

1. Retourne sur https://resend.com/domains
2. Attends que le status passe à "Verified" (✅ vert)
3. Si ça reste "Pending" après 30 min, clique "Verify" manuellement

---

## ⚠️ IMPORTANT - Ne PAS envoyer tant que:

- [ ] SPF vérifié (✅ vert)
- [ ] DKIM vérifié (✅ vert)
- [ ] DMARC configuré
- [ ] Domaine status = "Verified" dans Resend

**Envoyer sans vérification = spam garanti + potentiel blacklist définitif**

---

## 📧 Test après setup

Envoie 1 email test à:
- mail-tester.com (donne un score /10)
- Ta propre Gmail (vérifier si spam folder)
- Outlook/Hotmail (vérifier délivrabilité)

**Target: Score mail-tester ≥ 9/10**

---

**Prochaine étape**: Warm-up stratégique (voir WARM-UP-STRATEGY.md)
