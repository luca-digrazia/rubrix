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
  <ReInputContainer class="searchbar">
    <svgicon v-if="!filter" name="search" width="20" height="40" />
    <svgicon
      v-else
      class="searchbar__button"
      name="close"
      width="20"
      height="14"
      @click="filter = undefined"
    />
    <ReInput v-model="filter" :placeholder="placeholder" />
  </ReInputContainer>
</template>
<script>
import "assets/icons/search";
import "assets/icons/close";

export default {
  props: {
    placeholder: {
      type: String,
      default: "Search",
    },
  },
  data() {
    return { filter: this.value };
  },
  watch: {
    filter(val) {
      this.$emit("input", val);
    },
  },
};
</script>
<style lang="scss" scoped>
.searchbar {
  width: 285px;
  min-height: 43px;
  border: none;
  padding: 0 1em;
  display: flex;
  align-items: center;
  transition: all 0.2s ease;
  margin-right: auto;
  margin-left: 0;
  pointer-events: all;
  border-radius: $border-radius;
  @include font-size(14px);
  .svg-icon {
    fill: $font-secondary;
    margin: auto 1em auto 1em;
  }
  &__button {
    cursor: pointer;
  }
}
</style>
