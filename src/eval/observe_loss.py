import matplotlib.pyplot as plt
import pandas as pd


def load_and_process_data(csv_path: str, loss_col_name: str) -> pd.DataFrame:
    """
    Load data from a CSV file and calculate the average loss per epoch.

    :param csv_path: Path to the CSV file containing train or validation loss data
    :param loss_col_name: Name of the column containing loss values
    :return: DataFrame with average loss data per epoch
    """
    loss_df = pd.read_csv(csv_path)
    epoch_loss = loss_df.groupby("epoch_number")[loss_col_name].mean().reset_index()
    return epoch_loss


def plot_loss_curves(
    train_epoch_loss: pd.DataFrame, val_epoch_loss: pd.DataFrame, save_path: str
) -> None:
    """
    Plot training and validation loss curves.

    :param train_epoch_loss: DataFrame with average training loss data
    :param val_epoch_loss: DataFrame with average validation loss data
    :param save_path: Optional path to save the plot as a PNG file
    """
    plt.figure(figsize=(12, 6))
    plt.plot(
        train_epoch_loss["epoch_number"],
        train_epoch_loss["training_loss"],
        marker="o",
        label="Training Loss",
    )
    plt.plot(
        val_epoch_loss["epoch_number"],
        val_epoch_loss["validation_loss"],
        marker="s",
        label="Validation Loss",
    )
    plt.title("Average Training and Validation Loss per Epoch")
    plt.xlabel("Epochs")
    plt.ylabel("Average Loss")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved as {save_path}")

    plt.show()


def main() -> None:
    train_file = "../../result/step_wise_training_metrics.csv"
    val_file = "../../result/validation_metrics.csv"
    save_path = "./loss_curves.png"

    train_epoch_loss = load_and_process_data(train_file, "training_loss")
    val_epoch_loss = load_and_process_data(val_file, "validation_loss")
    plot_loss_curves(train_epoch_loss, val_epoch_loss, save_path)


if __name__ == "__main__":
    main()
