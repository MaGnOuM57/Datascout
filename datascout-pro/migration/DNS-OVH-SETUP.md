# Configuration DNS OVH pour ellievai.com

## 🎯 Records à Ajouter

Tu vas te connecter sur **OVH Manager**: https://www.ovh.com/manager/

1. Va dans **Web Cloud** → **Noms de domaine** → **ellievai.com**
2. Onglet **Zone DNS**
3. Clique **Ajouter une entrée**

---

## ✉️ RECORDS EMAIL (Resend via Amazon SES)

### Record 1: MX (Mail Exchange)
```
Type: MX
Sous-domaine: (vide) ou @
Cible: feedback-smtp.eu-west-1.amazonses.com
Priorité: 10
TTL: 3600
```

---

### Record 2: SPF (Sender Policy Framework)
```
Type: TXT
Sous-domaine: (vide) ou @
Valeur: v=spf1 include:amazonses.com ~all
TTL: 3600
```

---

### Record 3: DKIM (DomainKeys Identified Mail)
```
Type: TXT
Sous-domaine: resend._domainkey
Valeur: p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDe+glSbi2aTCB3EHLS99SYeJ0/BQYIZEGgppKPEem2k0RXKQfZIX0GcTUnxN3sW9d1dQ/bnYK0QR6z4DDiz0hdWcRp4FLRGmIlC3Y7E1xqSVn79pva7bp17Tu6o9EC3s+x8XQq0Que/clG3wyFIs7hapTK3+TWzOvqkXD7ZhBGQQIDAQAB
TTL: 3600
```

**⚠️ IMPORTANT**: Dans OVH, le champ "Sous-domaine" doit être: **resend._domainkey**

---

### Record 4: DMARC (Domain-based Message Authentication)
```
Type: TXT
Sous-domaine: _dmarc
Valeur: v=DMARC1; p=quarantine; rua=mailto:contact@ellievai.com; pct=100; adkim=s; aspf=s
TTL: 3600
```

---

## 🌐 RECORDS VERCEL (pour le site)

### Record 5: CNAME pour www
```
Type: CNAME
Sous-domaine: www
Cible: cname.vercel-dns.com.
TTL: 3600
```

**⚠️ Note**: Le point final (.) après `.com` est important

---

### Record 6: A (racine domaine)
```
Type: A
Sous-domaine: (vide) ou @
Cible: 76.76.21.21
TTL: 3600
```

**OU si OVH propose ALIAS/ANAME**:
```
Type: ALIAS
Sous-domaine: @
Cible: cname.vercel-dns.com
```

---

## ✅ Vérification après config (5-30 min propagation)

### Via terminal:
```bash
# SPF
dig TXT ellievai.com +short

# DKIM
dig TXT resend._domainkey.ellievai.com +short

# DMARC
dig TXT _dmarc.ellievai.com +short

# MX
dig MX ellievai.com +short

# Vercel
dig ellievai.com +short
dig www.ellievai.com +short
```

### Via web:
- https://mxtoolbox.com/SuperTool.aspx (tape ellievai.com)
- https://www.mail-tester.com (envoie email test)

---

## 🚨 Problèmes courants OVH

### Si tu as déjà des records MX/SPF:
1. **SUPPRIME les anciens records MX** (sinon conflit)
2. **Remplace l'ancien SPF** (pas d'ajout, remplacement)
3. OVH accepte max 1 seul record SPF par domaine

### Si propagation lente:
- Attends 1-2h max (OVH est parfois lent)
- Force refresh cache DNS local: `sudo systemd-resolve --flush-caches`

### Si DKIM fail:
- Vérifie que sous-domaine = exactement `resend._domainkey` (pas de typo)
- Vérifie que valeur commence par `p=` (pas `v=DKIM1; p=`)

---

## 📸 Screenshots OVH à faire:

1. Onglet Zone DNS avec tous les records visibles
2. Envoie-moi screenshot pour validation

---

**Temps total**: 10 min config + 5-30 min propagation DNS
