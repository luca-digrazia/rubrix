<!--
  - coding=utf-8
  - Copyright 2021-present, the Recognai S.L. team.
  -
  - Licensed under the Apache License, Version 2.0 (the "License");
  - you may not use this file except in compliance with the License.
  - You may obtain a copy of the License at
  -
  -     http://www.apache.org/licenses/LICENSE-2.0
  -
  - Unless required by applicable law or agreed to in writing, software
  - distributed under the License is distributed on an "AS IS" BASIS,
  - WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  - See the License for the specific language governing permissions and
  - limitations under the License.
  -->

<template>
  <input
    class="re-input"
    :type="type"
    :name="name"
    :value="value"
    :disabled="disabled"
    :required="required"
    :placeholder="placeholder"
    :maxlength="maxlength"
    :readonly="readonly"
    @focus="onFocus"
    @blur="onBlur"
    @input="onInput"
    @keydown.up="onInput"
    @keydown.down="onInput"
  />
</template>

<script>
import common from "./common";
import getClosestVueParent from "~/components/core/utils/getClosestVueParent";

export default {
  mixins: [common],
  props: {
    type: {
      type: String,
      default: "text",
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.parentContainer = getClosestVueParent(
        this.$parent,
        "re-input-container"
      );

      if (!this.parentContainer) {
        this.$destroy();

        throw new Error("You should wrap the re-input in a re-input-container");
      }

      this.parentContainer.inputInstance = this;
      this.setParentDisabled();
      this.setParentRequired();
      this.setParentPlaceholder();
      this.handleMaxLength();
      this.updateValues();
    });
  },
};
</script>
