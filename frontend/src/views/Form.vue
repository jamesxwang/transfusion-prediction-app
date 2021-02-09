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
            <el-select v-model.number="form['性别（1=男，0=女）']" placeholder="Gender">
              <el-option
                v-for="item in gender"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Age:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input v-model.number="form['年龄']" placeholder="Age"></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Height(cm):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input type="number" v-model.number="data['Height(cm)']" placeholder="Height(cm)"></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Weight(kg):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input type="number" v-model.number="data['Weight(cm)']" placeholder="Weight(kg)"></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Blood type:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model="form['血型']" placeholder="Blood Type">
              <el-option
                v-for="item in blood_type"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <div class="step step_two" v-if="active===1">
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Atrial Fibrillation:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['心房颤动（有选1，否选0）']" placeholder="Atrial Fibrillation">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Left Ventricular Enlargement:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select
              v-model.number="form['左心室扩大（有选1，否选0）']"
              placeholder="Left Ventricular Enlargement"
            >
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Treated Hypertension:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['高血压史']" placeholder="Treated Hypertension">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Diabetes mellitus:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['糖尿病史']" placeholder="Diabetes mellitus">
              <el-option
                v-for="item in yes_or_no"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row>
          <el-col
            :xs="12"
            :sm="12"
            :md="10"
            :lg="14"
            :xl="14"
          >NYHA classification (New York Heart Association Classification):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-select v-model.number="form['NYHA心功能分级']" placeholder="NYHA classification">
              <el-option v-for="i in 4" :key="i" :value="i" :label="i"></el-option>
            </el-select>
          </el-col>
        </el-row>
      </div>
      <div class="step step_three" v-if="active>=2">
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">White Blood Cell(WBC, 10^9/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前白细胞（10^9/L)']"
              placeholder="White Blood Cell(WBC, 10^9/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Platelet Count (PLT, 10^9/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前血小板计数（10^9/L)']"
              placeholder="Platelet Count (PLT, 10^9/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Hemoglobin (Hb, g/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前血红蛋白（g/L）']"
              placeholder="Hemoglobin (Hb, g/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col
            :xs="12"
            :sm="12"
            :md="10"
            :lg="14"
            :xl="14"
          >Extracorporeal circulation priming volume (mL):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['体外循环预充量（ml）']"
              placeholder="Extracorporeal circulation priming volume (mL)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Serum creatinine(Scr,mol/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前肌酐（umol/L ） ']"
              placeholder="Serum creatinine(Scr,mol/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Albumin(ALB, g/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前白蛋白（g/L）']"
              placeholder="Albumin(ALB, g/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">Alanine Transaminase (ALT, U/L):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前谷丙转氨酶（IU/L）']"
              placeholder="Alanine Transaminase (ALT, U/L)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col
            :xs="12"
            :sm="12"
            :md="10"
            :lg="14"
            :xl="14"
          >Left ventricular ejection fraction(LVEF, %):</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前左心室射血分数（%）']"
              placeholder="Left ventricular ejection fraction(LVEF, %)"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="10" :lg="14" :xl="14">International Normalized Ratio（INR）:</el-col>
          <el-col :xs="12" :sm="8" :md="12" :lg="8" :xl="8">
            <el-input
              type="number"
              v-model.number="form['术前INR']"
              placeholder="International Normalized Ratio（INR）"
            ></el-input>
          </el-col>
        </el-row>
      </div>
      <div class="button_container">
        <el-button
          style="margin-top: 12px;"
          @click="previous"
          v-if="active>0"
          icon="el-icon-arrow-left"
        >Previous</el-button>
        <el-button
          style="margin-top: 12px;"
          @click="submit"
          v-if="active===3"
          type="success"
          v-loading.fullscreen.lock="fullscreenLoading"
        >Predict</el-button>
        <el-button style="margin-top: 12px;" @click="next" v-if="active<3" type="primary">
          Next Step
          <i class="el-icon-arrow-right el-icon--right"></i>
        </el-button>
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
.el-select,
.el-input {
  width: 100%;
}
.el-row {
  margin: 1em 0;
}
.form_container {
  border-radius: 8px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  padding: 2em;
  & .step {
    min-height: 40vh;
  }
  .button_container {
    text-align: right;
  }
}
div {
  margin: 0;
}
</style>

<script>
import translation from "../locale/translate";

export default {
  name: "form",
  data() {
    return {
      active: 0,
      gender: [
        { value: 1, label: "Male" },
        { value: 0, label: "Female" }
      ],
      blood_type: [
        { value: 1, label: "A" },
        { value: 2, label: "B" },
        { value: 3, label: "O" },
        { value: 4, label: "AB" }
      ],
      yes_or_no: [
        { value: 1, label: "Yes" },
        { value: 0, label: "No" }
      ],
      data: {
        "Height(cm)": "",
        "Weight(cm)": ""
      },
      form: {
        "性别（1=男，0=女）": "",
        年龄: "",
        BMI: "",
        血型: "",
        "心房颤动（有选1，否选0）": "",
        "左心室扩大（有选1，否选0）": "",
        高血压史: "",
        糖尿病史: "",
        NYHA心功能分级: "",
        "体外循环预充量（ml）": "",
        "术前白细胞（10^9/L)": "",
        "术前血红蛋白（g/L）": "",
        "术前血小板计数（10^9/L)": "",
        "术前肌酐（umol/L ） ": "",
        "术前白蛋白（g/L）": "",
        "术前谷丙转氨酶（IU/L）": "",
        "术前左心室射血分数（%）": "",
        "术前INR": "",
      },
      negativeChartData: [],
      positiveChartData: [],
      fullscreenLoading: false
    };
  },
  methods: {
    translate(chinese) {
      return translation[chinese];
    },
    validate() {
      let valid = true;
      for (let i in this.form) {
        if (typeof this.form[i] === "string") {
          this.$message.error(`${i} cannot be empty!`);
          valid = false;
          return valid;
        }
      }
      return valid;
    },
    next() {
      if (this.active++ > 1) this.active = 3;
    },
    previous() {
      if (this.active-- <= 0) this.active = 0;
    },
    submit() {
      this.fullscreenLoading = true;
      this.computeBMI();
      if (this.validate()) {
        this.postData().then(
          res => {
            console.log(res);

            let predictionResult = res.data;
            let negativeData = [];
            let positiveData = [];
            let categories = [];

            for (
              let i = 0, positive = predictionResult.data.positive;
              i < positive.length;
              i++
            ) {
              categories.push(this.translate(positive[i][0]));
              positiveData.push((positive[i][1] * 100).toFixed(2));
            }
            for (
              let i = 0, negative = predictionResult.data.negative;
              i < negative.length;
              i++
            ) {
              categories.push(this.translate(negative[i][0]));
              negativeData.push((negative[i][1] * -100).toFixed(2));
            }
            console.log("categories: ", categories);
            let temp = [0, 0, 0, 0, 0];
            negativeData = temp.concat(negativeData);
            positiveData = positiveData.concat(temp);
            let params = {
              rawData: predictionResult.data,
              result: predictionResult.result,
              prob: predictionResult.prob,
              negativeChartData: negativeData,
              positiveChartData: positiveData,
              categories: categories
            };
            this.fullscreenLoading = false;
            this.$router.push({
              name: "prediction",
              params
            });
          },
          error => {
            this.$message.error(error);
          }
        );
      }
    },
    postData() {
      return new Promise((resolve, reject) => {
        this.$axios({
          url: "api/predict",
          method: "post",
          data: { "0": this.form }
        })
          .then(res => {
            if (res.status == 200) {
              resolve(res.data);
            } else {
              reject(res.data);
            }
          })
          .catch(e => {
            reject(e);
          });
      });
    },
    computeBMI() {
      this.form["BMI"] =
        this.data["Weight(cm)"] / (this.data["Height(cm)"] / 100) ** 2;
    }
  }
};
</script>
