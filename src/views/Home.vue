<style scoped src="@/assets/styles/Home.css"></style>
<template>
  <div class="home-container">
    <div class="home" v-if="currentUserData">
      <div class="row columns">
        <column class="taskColumn">
          <h3 id="taskCol">ToDo  <i class="fas fa-clipboard-list"></i></h3>
          <draggable
            id="todos"
            class="list-group"
            :list="currentUserData.todos"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item todoTask"
              v-for="(todo, index) in currentUserData.todos"
              :itemid="todo.id"
              :key="index"
            >
              {{ todo.taskName }}
              <button
                class="btn btn-warning"
                @click="handleOnClickedEdit(todo)"
              >
                Edit
              </button>

              <button
                class="btn btn-danger"
                @click="handleOnClickedRemove(todo)"
              >
                X
              </button>
            </div>
          </draggable>
        </column>

        <column class="taskColumn">
          <h3 id="taskCol">In Progress  <i class="fas fa-spinner"></i></h3>

          <draggable
            id="inProgress"
            class="list-group"
            :list="currentUserData.inProgress"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item inProgTask"
              v-for="(todo, index) in currentUserData.inProgress"
              :key="todo.taskName"
              :itemid="todo.id"
            >
              {{ todo.taskName }}
              <button
                class="btn btn-warning"
                @click="handleOnClickedEdit(todo)"
              >
                Edit
              </button>

              <button
                class="btn btn-danger"
                @click="handleOnClickedRemove(todo)"
              >
                X
              </button>
            </div>
          </draggable>
        </column>

        <column class="taskColumn">
          <h3 id="taskCol">Revision  <i class="fab fa-rev"></i></h3>

          <draggable
            id="revision"
            class="list-group"
            :list="currentUserData.revision"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item revTask"
              v-for="(todo, index) in currentUserData.revision"
              :key="todo.taskName"
              :itemid="todo.id"
            >
              {{ todo.taskName }}
              <button
                class="btn btn-warning"
                @click="handleOnClickedEdit(todo)"
              >
                Edit
              </button>

              <button
                class="btn btn-danger"
                @click="handleOnClickedRemove(todo)"
              >
                X
              </button>
            </div>
          </draggable>
        </column>

        <column class="taskColumn">
          <h3 id="taskCol">Check  <i class="fas fa-user-check"></i></h3>

          <draggable
            id="check"
            class="list-group"
            :list="currentUserData.check"
            group="people"
            @change="log"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item checkTask"
              v-for="(todo, index) in currentUserData.check"
              :key="todo.taskName"
              :itemid="todo.id"
            >
              {{ todo.taskName }}
              <button
                class="btn btn-warning"
                @click="handleOnClickedEdit(todo)"
              >
                Edit
              </button>
              <button
                class="btn btn-danger"
                @click="handleOnClickedRemove(todo)"
              >
                X
              </button>
            </div>
          </draggable>
        </column>

        <column class="taskColumn">
          <h3 id="taskCol">Done  <i class="fas fa-check-double"></i></h3>

          <draggable
            id="done"
            class="list-group"
            :list="currentUserData.done"
            group="people"
            @change="log"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item doneTask"
              v-for="(todo, index) in currentUserData.done"
              :key="todo.taskName"
              :itemid="todo.id"
            >
              {{ todo.taskName }}
              <button
                class="btn btn-warning"
                @click="handleOnClickedEdit(todo)"
              >
                Edit
              </button>

              <button
                class="btn btn-danger"
                @click="handleOnClickedRemove(todo)"
              >
                X
              </button>
            </div>
          </draggable>
        </column>
      </div>
    </div>
    <button
      @click="$modal.show('task-modal')"
      class="add-todo-button btn btn-primary mt-3 btn-block mb-5"
    >
      Add todo
    </button>
    <button @click="logoutUser">Logout</button>
    <task-modal
      :selected-task="currentSelectedTask"
      @modal-closed="currentSelectedTask = null"
      @clicked-on-update="handleOnClickedOnTaskUpdate"
    />
  </div>
</template>
<script>
import draggable from "vuedraggable";
import Column from "@/components/Column";
import TaskModal from "@/components/TaskModal";
import { mapGetters, mapMutations } from "vuex";
import db from "@/database";
import firebase from "firebase";

export default {
  name: "Home",
  components: {
    draggable,
    Column,
    TaskModal,
  },
  data() {
    return {
      currentSelectedTask: null,
    };
  },
  computed: {
    ...mapGetters(["currentUserData", "currentUser"]),
  },
  methods: {
    ...mapMutations(["setCurrentUserHandler", "setCurrentUserDataHandler"]),
    logoutUser() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.setCurrentUserHandler(null);
          this.setCurrentUserDataHandler(null);
          // Sign-out successful.
        })
        .catch((error) => {
          // An error happened.
        });
    },
    handleOnClickedRemove(task) {
      let taskIdx = this.currentUserData[task.state].findIndex(
        (x) => x.id === task.id
      );
      if (taskIdx > -1) {
        this.currentUserData[task.state].splice(taskIdx, 1);
        // this.$(this.currentUserData[task.state], taskIdx, task);
        this.updateCurrentUsersTasks();
      }
    },
    handleOnClickedOnTaskUpdate(task) {
      // task.state = todos, inProgress...
      console.log(task);
      let taskIdx = this.currentUserData[task.state].findIndex(
        (x) => x.id === task.id
      );
      if (taskIdx > -1) {
        delete this.currentUserData[taskIdx];
        this.$set(this.currentUserData[task.state], taskIdx, task);
        this.updateCurrentUsersTasks();
      }
    },
    handleOnClickedEdit(task) {
      this.currentSelectedTask = task;
      this.$modal.show("task-modal");
    },
    updateCurrentUsersTasks(task) {
      let userRef = db.collection("users").doc(this.currentUser.uid);
      userRef
        .update({
          ...this.currentUserData,
        })
        .then(function() {
          console.log("Document successfully written!");
        })
        .catch(function(error) {
          console.error("Error writing document: ", error);
        });
    },
    handleOnAdd(event) {
      console.log("event", event);
      let itemId = event.item.getAttribute("itemid");

      // event.to.id = todos, inProgress, revision...
      let idx = this.currentUserData[event.to.id].findIndex(
        (x) => x.id === itemId
      );

      if (idx > -1) {
        this.currentUserData[event.to.id][idx].state = event.to.id;
      }
    },
    log(evt) {
      window.console.log(evt);
      this.updateCurrentUsersTasks();
    },
  },
};
</script>
