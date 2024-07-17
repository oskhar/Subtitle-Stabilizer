<!-- src/App.vue -->
<template>
  <v-app>
    <v-main>
      <v-container>
        <v-card class="pa-4">
          <v-card-title>Subtitle Time Updater</v-card-title>
          <v-card-text>
            <v-file-input
              label="Select Subtitle File"
              v-model="file"
              accept=".srt"
            ></v-file-input>
            <v-text-field
              label="Offset (HH:MM:SS,mmm)"
              v-model="offset"
            ></v-text-field>
            <v-select
              v-model="operation"
              :items="operations"
              label="Operation"
            ></v-select>
            <v-btn @click="processFile">Update Subtitle</v-btn>
            <v-btn
              v-if="downloadUrl"
              :href="downloadUrl"
              download="updated_subtitle.srt"
              >Download Updated Subtitle</v-btn
            >
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const file = ref(null);
    const offset = ref("00:00:00,000");
    const operation = ref("add");
    const operations = ["add", "subtract"];
    const downloadUrl = ref("");

    const processFile = () => {
      if (!file.value) {
        alert("Please select a subtitle file.");
        return;
      }

      const reader = new FileReader();
      reader.onload = (event) => {
        const content = event.target.result;
        const updatedContent = updateSubtitleTime(
          content,
          offset.value,
          operation.value
        );
        const blob = new Blob([updatedContent], { type: "text/plain" });
        downloadUrl.value = URL.createObjectURL(blob);
      };
      reader.readAsText(file.value);
    };

    const strToMilliseconds = (timeStr) => {
      const [hours, minutes, seconds] = timeStr.split(":");
      const [secs, millis] = seconds.split(",");
      return (
        (parseInt(hours) * 3600 + parseInt(minutes) * 60 + parseInt(secs)) *
          1000 +
        parseInt(millis)
      );
    };

    const millisecondsToStr = (ms) => {
      const hours = String(Math.floor(ms / 3600000)).padStart(2, "0");
      ms %= 3600000;
      const minutes = String(Math.floor(ms / 60000)).padStart(2, "0");
      ms %= 60000;
      const seconds = String(Math.floor(ms / 1000)).padStart(2, "0");
      const millis = String(ms % 1000).padStart(3, "0");
      return `${hours}:${minutes}:${seconds},${millis}`;
    };

    const updateSubtitleTime = (content, offsetStr, operation) => {
      const offsetMs = strToMilliseconds(offsetStr);
      const timePattern =
        /(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})/g;
      return content.replace(timePattern, (match, start, end) => {
        let newStart = strToMilliseconds(start);
        let newEnd = strToMilliseconds(end);

        if (operation === "add") {
          newStart += offsetMs;
          newEnd += offsetMs;
        } else {
          newStart -= offsetMs;
          newEnd -= offsetMs;
        }

        return `${millisecondsToStr(newStart)} --> ${millisecondsToStr(
          newEnd
        )}`;
      });
    };

    return {
      file,
      offset,
      operation,
      operations,
      processFile,
      downloadUrl,
    };
  },
};
</script>
