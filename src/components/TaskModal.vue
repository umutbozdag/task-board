<template>
  <modal
    name="task-modal"
    adaptive
    :width="700"
    :height="700"
    @opened="handleOnOpened"
    @closed="handleOnClosed"
  >
    <div class="p-3">
      <h2 class="text-center">Add task</h2>
      <div class="row mt-4">
        <div class="col-lg-8">
          <input
            v-model="taskName"
            type="text"
            placeholder="Task name"
            class="form-control"
          />
        </div>
        <div class="col-lg-4" v-if="status === 'update' && selectedTask">
          <label for="" class="">State:</label>
          <input
            type="text"
            disabled
            class="form-control ml-2"
            :placeholder="selectedTask.state"
          />
        </div>
      </div>

      <div class="row mt-3 mb-3">
        <div class="col-lg-12">
          <textarea
            v-model="taskNotes"
            name=""
            id=""
            class="form-control"
            placeholder="Task notes"
          ></textarea>
        </div>
      </div>

      <div class="row mt-3 mb-3">
        <div class="col-lg-12">
          <textarea
            name=""
            id=""
            v-model="taskDesc"
            class="form-control"
            placeholder="Task description"
          ></textarea>
        </div>
      </div>
      <div class="row d-flex align-items-center">
        <div class="col-lg-4">
          <date-pick v-model="taskCreateDate"></date-pick>
        </div>
        <div class="col-lg-4">
          <input
            type="text"
            placeholder="5 gun"
            disabled
            class="form-control"
          />
        </div>
        <div class="col-lg-4">
          <label for="">Real date</label>
          <input
            type="text"
            :placeholder="taskCreateDate"
            disabled
            class="form-control"
          />
        </div>
      </div>
      <button
        v-if="status === 'new'"
        @click="createTask"
        class="btn btn-primary btn-block mt-4 col-12"
      >
        Create
      </button>
      <button
        v-else
        @click="updateTask"
        class="btn btn-primary btn-block mt-4 col-12"
      >
        Update
      </button>
    </div>
  </modal>
</template>

<script>
import db from "@/database";
import firebase from "firebase";
import { mapActions, mapGetters, mapMutations } from "vuex";
import { v4 as uuidv4 } from "uuid";
import DatePick from "vue-date-pick";
import "vue-date-pick/dist/vueDatePick.css";

export default {
  name: "TaskModal",
  components: {
    DatePick,
  },
  props: {
    selectedTask: {
      type: Object,
    },
  },
  data() {
    return {
      priorities: null,
      taskCreateDate: this.dateOfToday,
      taskName: null,
      taskDesc: null,
      taskNotes: null,
      status: "new",
    };
  },
  computed: {
    ...mapGetters(["currentUser", "currentUserData"]),
    dateOfToday() {
      return new Date().toISOString().slice(0, 10);
    },
  },
  methods: {
    ...mapMutations(["setCurrentUserDataHandler"]),
    updateTask() {
      this.$emit("clicked-on-update", {
        taskCreateDate: this.taskCreateDate,
        taskName: this.taskName,
        taskDesc: this.taskDesc,
        taskNotes: this.taskNotes,
        id: this.selectedTask.id,
        state: this.selectedTask.state,
      });
      this.$modal.hide("task-modal");
    },
    handleOnOpened() {
      if (this.selectedTask) {
        this.status = "update";
        this.taskName = this.selectedTask.taskName;
        this.taskDesc = this.selectedTask.taskDesc;
        this.taskNotes = this.selectedTask.taskNotes;
        this.taskCreateDate = this.selectedTask.taskCreateDate;
      } else {
        this.status = "new";
      }
    },
    handleOnClosed() {
      this.status = "new";
      this.taskCreateDate = this.dateOfToday;
      this.$emit("modal-closed");
    },
    createTask() {
      if (this.currentUser) {
        let currentUserDocRef = db
          .collection("users")
          .doc(this.currentUser.uid);
        let todo = {
          taskName: this.taskName,
          taskDesc: this.taskDesc,
          taskNotes: this.taskNotes,
          taskCreateDate: this.taskCreateDate,
          id: uuidv4(),
          state: "todo",
        };

        console.log("todo", todo);
        // o anki kullanicinin array elementini guncelleme
        currentUserDocRef
          .update({
            todos: firebase.firestore.FieldValue.arrayUnion(todo),
          })
          .then(() => {
            console.log("update");
            this.setCurrentUserDataHandler({
              ...this.currentUserData,
              todos: [...this.currentUserData.todos, todo],
            });
            this.$modal.hide("task-modal");
          });
      }
    },
  },
  mounted() {
    if (this.dateOfToday) {
      this.taskCreateDate = this.dateOfToday;
    }
    // const priorities = [];
    // db.collection("priorities")
    //   .get()
    //   .then(function(querySnapshot) {
    //     querySnapshot.forEach((doc) => {
    //       // doc.data() is never undefined for query doc snapshots
    //       priorities.push(doc.data());
    //       console.log(doc.id, " => ", doc.data());
    //     });
    //   });
  },
};
</script>

<style lang="scss">
.vdpComponent {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  color: #303030;
}
.vdpWithInput > input {
  border-color: red;
  font-size: 16px;
  display: block;
  width: 100%;
  box-sizing: border-box;
  padding: 4px;
  padding-right: 40px;
  height: 38px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 4px;
  background: transparent;
  border: 1px solid #e0e0e0;
  box-shadow: 0 0.1em 0.3em rgba(0, 0, 0, 0.05);
  outline: 0;
}
</style>
