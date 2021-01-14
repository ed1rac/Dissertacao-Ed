class Policy {
        constructor(name, kp, org, sr, aa, ov, derivated, origin) {
            if (this.name === undefined) {
                this.name = null;
            }
            if (this.kp === undefined) {
                this.kp = null;
            }
            if (this.org === undefined) {
                this.org = null;
            }
            if (this.sr === undefined) {
                this.sr = null;
            }
            if (this.aa === undefined) {
                this.aa = null;
            }
            if (this.ov === undefined) {
                this.ov = null;
            }
            if (this.derivated === undefined) {
                this.derivated = false;
            }
            if (this.origin === undefined) {
                this.origin = null;
            }
            this.name = name;
            this.kp = kp;
            this.org = org;
            this.sr = sr;
            this.aa = aa;
            this.ov = ov;
            this.derivated = derivated;
            this.origin = origin;
        }
        setOrigin(origin) {
            this.origin = origin;
        }
        getOrigin() {
            return this.origin;
        }
        getName() {
            return this.name;
        }
        getOriginalName() {
            var parts = this.name.split("\\.");
            return parts[0];
        }
        setName(name) {
            this.name = name;
        }
        getKp() {
            return this.kp;
        }
        setKp(kp) {
            this.kp = kp;
        }
        getOrg() {
            if (this.org != null)
                return this.org;

            else
                return "";
        }
        setOrg(org) {
            this.org = org;
        }
        getSr() {
            if (this.sr != null)
                return this.sr;

            else
                return "null";
        }
        setSr(sr) {
            this.sr = sr;
        }
        getAa() {
            return this.aa;
        }
        setAa(aa) {
            this.aa = aa;
        }
        getOv() {
            return this.ov;
        }
        setOv(ov) {
            this.ov = ov;
        }
        setDerivated(derivated) {
            this.derivated = derivated;
        }
        isDerivated() {
            return this.derivated;
        }
        /**
             *
             * @return {string}
             */
        toString() {
            return this.name + "-> [" + this.kp + ", " + this.org + ", " + this.sr + ", " + this.aa + ", " + this.ov + "]";
        }
    }
    //return Policie;
