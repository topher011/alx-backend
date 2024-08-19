import kue from 'kue';

const my_queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

my_queue.process('push_notification_code', function(job, done) {
    const {phoneNumber, message} = job.data
    sendNotification(phoneNumber, message);
    done();
})
