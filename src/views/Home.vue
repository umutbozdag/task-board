<template>
  <div class="home-container">
    <div class="home" v-if="currentUserData">
      <div class="row columns">
        <column title="Todo">
          <draggable
            id="todos"
            class="list-group"
            :list="currentUserData.todos"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item"
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
            </div>
          </draggable>
        </column>

        <column title="In progress">
          <draggable
            id="inProgress"
            class="list-group"
            :list="currentUserData.inProgress"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item"
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
            </div>
          </draggable>
        </column>

        <column title="Revision">
          <draggable
            id="revision"
            class="list-group"
            :list="currentUserData.revision"
            @change="log"
            group="people"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item"
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
            </div>
          </draggable>
        </column>

        <column title="Check">
          <draggable
            id="check"
            class="list-group"
            :list="currentUserData.check"
            group="people"
            @change="log"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item"
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
            </div>
          </draggable>
        </column>

        <column title="Done">
          <draggable
            id="done"
            class="list-group"
            :list="currentUserData.done"
            group="people"
            @change="log"
            @add="handleOnAdd"
          >
            <div
              class="list-group-item"
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
            </div>
          </draggable>
        </column>

        <!-- <column title="Revision">
          <draggable
            class="list-group"
            :list="list3"
            group="people"
            @change="log"
          >
            <div
              class="list-group-item"
              v-for="(element, index) in list2"
              :key="element.name"
            >
              {{ element.name }} {{ index }}
            </div>
          </draggable>
        </column> -->
      </div>
    </div>
    <button
      @click="$modal.show('task-modal')"
      class="add-todo-button btn btn-primary mt-3 btn-block mb-5"
    >
      Add todo
    </button>
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
import { mapGetters } from "vuex";
import db from "@/database";

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
    handleOnClickedOnTaskUpdate(task) {
      // task.state = todos, inProgress...
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
<style lang="scss">
.column {
  margin-right: 24px;
}

.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: whitesmoke;
}

.home {
  height: 100%;
  padding: 40px;
}

.list-group-item {
  margin-bottom: 12px;
  box-shadow: 1px 1px 4px 0px rgba(0, 0, 0, 0.75);
}

.add-todo-button {
}

.columns {
  display: flex;
}

.list-group {
  height: 500px;
}
</style>
