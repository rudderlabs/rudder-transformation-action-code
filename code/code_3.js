export function transformEvent(event, metadata) {
  event.x = event.invalid.prop;
  return event;
}
