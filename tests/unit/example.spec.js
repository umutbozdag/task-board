import { shallowMount } from "@vue/test-utils";
import Login from "@/views/Login.vue";

describe("Login.vue", () => {
  it("testing!", async () => {
    const wrapper = shallowMount(Login, {
      data() {
        return {
          email: "email@hotmail.com",
          password: "test123",
        };
      },
      stubs: ["router-link"],
    });
    await wrapper.find("button").trigger("click");

    expect(wrapper.text()).toContain("Todo");
  });
});
