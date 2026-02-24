import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.disposables.Disposable;

public class RxJavaExample {
    public static void main(String[] args) {
        // Create an Observable that emits a sequence of integers
        Observable<Integer> observable = Observable.range(1, 5);

        // Create a Subscriber that consumes the emitted integers
        Observer<Integer> subscriber = new Observer<Integer>() {
            @Override
            public void onSubscribe(Disposable d) {
                System.out.println("Subscribed");
            }

            @Override
            public void onNext(Integer value) {
                System.out.println("Received: " + value);
            }

            @Override
            public void onError(Throwable e) {
                System.out.println("Error: " + e.getMessage());
            }

            @Override
            public void onComplete() {
                System.out.println("Completed");
            }
        };

        // Subscribe the Subscriber to the Observable
        observable.subscribe(subscriber);
    }
}
