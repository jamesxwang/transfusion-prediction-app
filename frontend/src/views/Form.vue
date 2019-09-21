<template>
  <div class="main_container">
    <div class="step_container">
      <el-steps :active="active" finish-status="success">
        <el-step title="Step 1"></el-step>
        <el-step title="Step 2"></el-step>
        <el-step title="Step 3"></el-step>
      </el-steps>
    </div>
    <div class="form_container">
      <div class="step step_one" v-if="active===0">
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Gender:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="data.gender" placeholder="Gender">
              <el-option
                v-for="item in gender"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Age:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Age']" placeholder="Age"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Height(cm):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Height(cm)']" placeholder="Height(cm)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Weight(kg):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Weight(cm)']" placeholder="Weight(kg)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Blood type:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model="data.blood_type" placeholder="Blood Type">
              <el-option
                v-for="item in blood_type"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <div class="step step_two" v-if="active===1">
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Atrial Fibrillation:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Atrial Fibrillation']" placeholder="Atrial Fibrillation">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Left Ventricular Enlargement:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Left Ventricular Enlargement']" placeholder="Left Ventricular Enlargement">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Treated Hypertension:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Treated Hypertension']" placeholder="Treated Hypertension">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Diabetes mellitus:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Diabetes mellitus']" placeholder="Diabetes mellitus">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Anemia (&lt; 13g/dL for males /&lt; 12g/dL for females respectively):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Anemia']" placeholder="Anemia">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Cerebrovascular diseases:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['Cerebrovascular diseases']" placeholder="Cerebrovascular diseases">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">NYHA classification (New York Heart Association Classification):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['NYHA classification']" placeholder="NYHA classification">
              <el-option v-for="i in 4" :key="i" :value=i :label="i"></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">ASA classification (American society of Anesthesiologists):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['ASA classification']" placeholder="ASA classification">
              <el-option v-for="i in 4" :key="i" :value=i :label="i"></el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <div class="step step_three" v-if="active>=2">
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Extracorporeal circulation priming volume (mL):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Extracorporeal circulation priming volume (mL)']" placeholder="Extracorporeal circulation priming volume (mL)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Red Blood Cell (RBC, 10^12/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Red Blood Cell (RBC, 10^12\/L)']" placeholder="Red Blood Cell (RBC, 10^12/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">White Blood Cell(WBC, 10^9/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['White Blood Cell(WBC, 10^9\/L)']" placeholder="White Blood Cell(WBC, 10^9/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Platelet Count (PLT, 10^9/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Platelet Count (PLT, 10^9\/L)']" placeholder="Platelet Count (PLT, 10^9/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Hemoglobin (Hb, g/dL):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Hemoglobin (Hb, g\/dL)']" placeholder="Hemoglobin (Hb, g/dL)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Hematocrit (HCT, %):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Hematocrit (HCT, %)']" placeholder="Hematocrit (HCT, %)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Serum creatinine(Scr,mol/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Serum creatinine(Scr,mol\/L )']" placeholder="Serum creatinine(Scr,mol/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Total protein(TP, g/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Total protein(TP, g\/L)']" placeholder="Total protein(TP, g/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Albumin(ALB, g/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Albumin(ALB, g\/L)']" placeholder="Albumin(ALB, g/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Globulin(GLO, g/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Globulin(GLO, g\/L)']" placeholder="Globulin(GLO, g/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Aspertate Aminotransferase(AST, U/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Aspertate Aminotransferase(AST, U\/L)']" placeholder="Aspertate Aminotransferase(AST, U/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Alanine Transaminase (ALT, U/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Alanine Transaminase (ALT, U\/L)']" placeholder="Alanine Transaminase (ALT, U/L)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Prothrombin(PT, s):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['Prothrombin(PT, s)']" placeholder="Prothrombin(PT, s)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">International Normalized Ratio(INR):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input v-model.number="form['INR International Normalized Ratio(INR)']" placeholder="International Normalized Ratio(INR)"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Left ventricular ejection fraction(LVEF, %):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8"><el-input type="number" v-model.number="form['Left ventricular ejection fraction(LVEF, %)']" placeholder="Left ventricular ejection fraction(LVEF, %)"></el-input></el-col>
        </el-row>
      </div>
      <div class="button_container">
        <el-button style="margin-top: 12px;" @click="previous" v-if="active>0" icon="el-icon-arrow-left">Previous</el-button>
        <el-button style="margin-top: 12px;" @click="submit" v-if="active===3" type="success">Predict</el-button>
        <el-button style="margin-top: 12px;" @click="next" v-if="active<3" type="primary">Next Step<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main_container {
  width: 80%;
  margin: 2em auto;
  .step_container {
    margin: 0 0 2em 0;
  }
}
.el-select, .el-input{
  width: 100%;
}
.el-row {
  margin: 1em 0;
}
.form_container {
  border-radius: 8px;
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  padding: 2em;
  & .step {
    min-height: 40vh;
  }
  .button_container {
    text-align: right;
  }
}
div{
  margin: 0;
}
</style>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'form',
  components: {
    // HelloWorld
  },
  data() {
    return {
      active: 0,
      gender: [{value: 0, label: 'Male'},{value: 1, label: 'Female'}],
      blood_type: [{value: 1, label: 'A'}, {value: 2, label: 'B'},{value: 3, label: 'O'}, {value: 4, label: 'AB'}],
      yes_or_no: [{value: 1, label: 'Yes'}, {value: 0, label: 'No'}],
      data: {
        gender: '',
        blood_type: ''
      },
      form: {
        "Age": '',
        "Height(cm)": '',
        "Weight(cm)": '',
        "BMI": '',
        "Atrial Fibrillation": '',
        "Left Ventricular Enlargement": '',
        "Treated Hypertension": '',
        "Diabetes mellitus": '',
        "Anemia": '',
        "Cerebrovascular diseases": '',
        "NYHA classification": '',
        "ASA classification": '',
        "Extracorporeal circulation priming volume (mL)": '',
        "Red Blood Cell (RBC, 10^12\/L)": '',
        "White Blood Cell(WBC, 10^9\/L)": '',
        "Hemoglobin (Hb, g\/dL)": '',
        "Hematocrit (HCT, %)": '',
        "Platelet Count (PLT, 10^9\/L)": '',
        "Serum creatinine(Scr,mol\/L )": '',
        "Total protein(TP, g\/L)": '',
        "Albumin(ALB, g\/L)": '',
        "Globulin(GLO, g\/L)": '',
        "Alanine Transaminase (ALT, U\/L)": '',
        "Aspertate Aminotransferase(AST, U\/L)": '',
        "Prothrombin(PT, s)": '',
        "INR International Normalized Ratio(INR)": '',
        "Left ventricular ejection fraction(LVEF, %)": '',
        "Gender_female": '',
        "Gender_male": '' ,
        "Blood Type_A": '',
        "Blood Type_AB": '',
        "Blood Type_B": '',
        "Blood Type_O": '',
        "Extracorporeal circulation priming volume\/Body Mass Index": ''
      },
      negativeChartData: [],
      positiveChartData: [],
    }
  },
  methods: {
    validate() {
      let valid = true
      for (let i in this.form) {
        if (typeof this.form[i] === 'string') {
          this.$message.error(`${i} cannot be empty!`);
          valid = false
          return valid
        }
      }
      return valid
    },
    next() {
      if (this.active++ > 1) this.active = 3
    },
    previous() {
      if (this.active-- <= 0) this.active = 0
    },
    submit() {
      this.computeGender()
      this.computeBloodType()
      this.computeBMI()
      if (this.validate()) {
        this.postData().then(res => {
          console.log(res)
          let predictionResult = res.data
          let negativeData = []
          let positiveData = []
          let categories = []

          for (let i = 0, positive = predictionResult.data.positive; i < positive.length; i++) {
            categories.push(positive[i][0])
            positiveData.push((positive[i][1] * 100).toFixed(2))
          }
          for (let i = 0, negative = predictionResult.data.negative; i < negative.length; i++) {
            categories.push(negative[i][0])
            negativeData.push((negative[i][1] * (-100)).toFixed(2))
          }
          let temp = [0,0,0,0,0]
          negativeData = temp.concat(negativeData)
          positiveData = positiveData.concat(temp)
          let params = {
            result : predictionResult.result,
            negativeChartData: negativeData,
            positiveChartData: positiveData,
            categories: categories
          }
          this.$router.push({
            name: 'prediction',
            params
          })
        }, error => {
          this.$message.error(error)
        })
      }
    },
    postData() {
      return new Promise((resolve, reject) => {
        this.$axios({
          url: 'api/predict',
          method: 'post',
          data: {"0": this.form}
        }).then(res=>{
          if (res.status == 200) {
            resolve(res.data)
          } else {
            reject(res.data)
          }
        }).catch(e=>{
          reject(e)
        })
      })
    },
    computeGender() {
      if (this.data.gender === 0) {
        this.form.Gender_female = 0
        this.form.Gender_male = 1
      } else if (this.data.gender === 1){
        this.form.Gender_female = 1
        this.form.Gender_male = 0
      }
    },
    computeBloodType() {
      this.form['Blood Type_A'] = 0
      this.form['Blood Type_B'] = 0
      this.form['Blood Type_O'] = 0
      this.form['Blood Type_AB'] = 0
      switch (this.data.blood_type) {
        case 1:
          this.form['Blood Type_A'] = 1
          break;
        case 2:
          this.form['Blood Type_B'] = 1
          break;
        case 3:
          this.form['Blood Type_O'] = 1
          break;
        case 4:
          this.form['Blood Type_AB'] = 1
          break;
        default:
          break;
      }
    },
    computeBMI() {
      this.form['BMI'] = this.form['Weight(cm)'] / ((this.form['Height(cm)'] / 100)**2)
      this.form['Extracorporeal circulation priming volume\/Body Mass Index'] = this.form['Extracorporeal circulation priming volume (mL)'] / this.form['BMI']
    }
  }
}
</script>
