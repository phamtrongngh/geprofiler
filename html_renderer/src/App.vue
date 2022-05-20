<template>
  <div id="app">
    <Header />
    <div class="margins" v-for="item in sessions" :key="item.start_time">
      <div class="row">
        <div class="metrics">
          <div class="metric-label">URL:</div>
          <div class="metric-value">{{ url(item) }}</div>
          <div class="metric-label">Recorded:</div>
          <div class="metric-value">{{ startTime(item) }}</div>
          <div class="metric-label">Duration:</div>
          <div class="metric-value">{{ duration(item) }} seconds</div>
          <div class="metric-label">CPU time:</div>
          <div class="metric-value">{{ cpuTime(item) }} seconds</div>
        </div>
      </div>
      <hr/>
      <Frame v-if="rootFrame(item)" :frame="rootFrame(item)" />
    </div>
  </div>
</template>

<script>
import Frame from "./Frame.vue";
import Header from "./Header.vue";
import FrameModel from "./model/Frame";
import appState from "./appState";

export default {
  name: "app",
  data() {
    return {
      appState,
      sessions: window.profileSession,
    };
  },
  mounted() {
    window.App = this;
    this.setFavicon(require("./assets/favicon.png"));
    if (!this.sessions) {
      // in dev mode, load a sample json.
      fetch("./sample.json")
        .then((response) => response.json())
        .then((sample) => {
          this.sessions = sample;
        })
        .catch(console.log);
    }

    this.scrollListener = () => this.didScroll();
    window.addEventListener("scroll", this.scrollListener, { passive: true });
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.scrollListener, {
      passive: true,
    });
  },
  methods: {
    didScroll() {
      // don't let the body scroll up due to lack of content (when a tree is closed)
      // prevents the frames from jumping around when they are collapsed
      document.body.style.minHeight = `${
        window.scrollY + window.innerHeight
      }px`;
    },
    setFavicon(image) {
      var link =
        document.querySelector("link[rel*='icon']") ||
        document.createElement("link");
      // link.type = 'image/x-icon';
      link.rel = "shortcut icon";
      link.href = image;
      document.getElementsByTagName("head")[0].appendChild(link);
    },
    startTime(item) {
      const date = new Date(item.start_time * 1000);
      return date.toLocaleString();
    },
    cpuTime(item) {
      return item.cpu_time.toLocaleString(undefined, {
        maximumSignificantDigits: 3,
      });
    },
    duration(item) {
      return item.duration.toLocaleString(undefined, {
        maximumSignificantDigits: 3,
      });
    },
    rootFrame(item) {
      if (item && item.root_frame) {
        return new FrameModel(item.root_frame);
      }
    },
    url(item) {
      return item.url || "UNKNOWN";
    },
  },
  components: {
    Frame,
    Header,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Source+Code+Pro:400,600|Source+Sans+Pro:400,600");

html,
body {
  background-color: #000000;
  color: white;
  padding: 0;
  margin: 0;
}

#app {
  font-family: "Source Sans Pro", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.margins {
  border: 2px solid rgb(35, 34, 34);
  background-color: #303538;
  padding: 0px 30px;
  margin: 16px 0;
}

.row {
  display: flex;
  align-items: center;
  margin: 20px 0;
}
.metrics {
  display: grid;
  grid-template-columns: auto auto auto auto;
  font-size: 16px;
  text-transform: uppercase;
  grid-gap: 1px 8px;
}

.metric-label {
  font-weight: 600;
  color: hsl(40deg 97% 54%);
}
.metric-value {
  color: #e7eff3;
  margin-right: 0.5em;
}
</style>
